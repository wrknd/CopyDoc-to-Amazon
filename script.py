import os
import shutil
from datetime import datetime
import pycountry
import curses
import questionary
from tqdm import tqdm

def select_directory():
    # Replace curses-based selection with questionary
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    available_dirs = [d for d in os.listdir(script_dir) 
                     if os.path.isdir(os.path.join(script_dir, d))
                     and not d.startswith('.')]
    
    if not available_dirs:
        print("No folders found in the script's directory.")
        print("Please create a folder with your ASIN files first.")
        return None
    
    selected_dir = questionary.select(
        "Select the source folder:",
        choices=sorted(available_dirs)
    ).ask()
    
    return os.path.join(script_dir, selected_dir) if selected_dir else None

def get_iso_country_code(language_code):
    # Extract the country code part after the hyphen
    if '-' in language_code:
        country_code = language_code.split('-')[1]
        try:
            # Try to get the alpha_2 code for the country
            country = pycountry.countries.get(alpha_2=country_code)
            if country:
                return country.alpha_2.lower()
        except:
            pass
    
    # Fallback mappings for special cases
    language_to_country = {
        'en': 'gb',  # Default English to GB
        'es': 'es',  # Default Spanish to Spain
        'pt': 'pt',  # Default Portuguese to Portugal
        'zh': 'cn',  # Default Chinese to China
        'ar': 'sa',  # Default Arabic to Saudi Arabia
    }
    
    # If no country code found, try to map based on language
    base_language = language_code.split('-')[0].lower()
    return language_to_country.get(base_language, base_language)

def reorganize_files():
    source_dir = select_directory()
    
    if not source_dir:
        print("No directory selected. Exiting...")
        return
    
    if not os.path.exists(source_dir):
        print("Directory does not exist. Exiting...")
        return

    # Create timestamp for target directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_base_dir = os.path.join(script_dir, f"Amazon_Upload_{timestamp}")
    
    print(f"Creating directory at: {target_base_dir}")
    os.makedirs(target_base_dir, exist_ok=True)

    # Get list of all files to process for progress bar
    files_to_process = []
    print(f"Scanning source directory: {source_dir}")
    for root, _, files in os.walk(source_dir):
        for file in files:
            if any(file.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png']):
                files_to_process.append((root, file))
    
    print(f"Found {len(files_to_process)} files to process")

    # Process files with progress bar
    with tqdm(total=len(files_to_process), desc="Processing files", unit="file") as pbar:
        for root, file in files_to_process:
            try:
                # Extract ASIN and language code
                name_part = os.path.splitext(file)[0]
                extension = os.path.splitext(file)[1]
                
                # Extract full ASIN including PT part (everything before the language code in parentheses)
                full_asin = name_part.split(' (')[0]
                # Extract base ASIN (first 10 characters) for folder structure
                base_asin = full_asin[:10]
                
                # Create new filename without the suffix
                new_file_name = full_asin + extension

                # Extract language code from parentheses
                if '(' in name_part and ')' in name_part:
                    lang_part = name_part.split('(')[1].split(')')[0]
                    if '(Copy of Original Frame)' in name_part:
                        # Place copies in a separate folder
                        country_dir = os.path.join(target_base_dir, "Copy of Original")
                        asin_dir = os.path.join(country_dir, base_asin)
                    elif lang_part:  # Handle any valid language code
                        country_dir = os.path.join(target_base_dir, get_iso_country_code(lang_part))
                        asin_dir = os.path.join(country_dir, base_asin)
                    else:
                        print(f"Skipping file with missing language code: {file}")
                        pbar.update(1)
                        continue
                else:
                    print(f"Skipping file with invalid format: {file}")
                    pbar.update(1)
                    continue

                # Create necessary directories
                os.makedirs(asin_dir, exist_ok=True)

                # Copy file to new location with clean filename
                source_file = os.path.join(root, file)
                target_file = os.path.join(asin_dir, new_file_name)
                
                shutil.copy2(source_file, target_file)
                print(f"Copied: {file} -> {target_file}")

            except Exception as e:
                print(f"Error processing {file}: {str(e)}")

            pbar.update(1)

    if os.path.exists(target_base_dir):
        print(f"\nFiles have been reorganized in: {target_base_dir}")
        print(f"Directory contents:")
        for root, dirs, files in os.walk(target_base_dir):
            level = root.replace(target_base_dir, '').count(os.sep)
            indent = ' ' * 4 * level
            print(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print(f"{subindent}{f}")
    else:
        print(f"\nError: Target directory was not created: {target_base_dir}")

if __name__ == "__main__":
    reorganize_files()