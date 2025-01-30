# CopyDoc-to-Amazon

This guide will help you use this tool to copy documents with proper country code formatting. Don't worry if you're not tech-savvy - we'll go through everything step by step!

## Prerequisites (What You Need Before Starting)

1. Install Visual Studio Code (VS Code)
   - Go to https://code.visualstudio.com/
   - Click the big blue "Download" button for your system (Windows, Mac, or Linux)
   - Double-click the downloaded file and follow the installation wizard

2. Install Python
   - Go to https://www.python.org/downloads/
   - Click "Download Python" (get the latest version)
   - During installation, **IMPORTANT**: Check the box that says "Add Python to PATH"

## Setting Up Your Environment (One-Time Setup)

1. Open VS Code
   - Click the Windows Start button or Mac Spotlight
   - Type "Visual Studio Code" and click to open it

2. Install Python Extension in VS Code
   - Click the square icon on the left sidebar (Extensions)
   - Search for "Python"
   - Install the one by Microsoft (it should be the first result)

3. Install Required Package
   - Press `Ctrl + ~` (Windows/Linux) or `Cmd + ~` (Mac) to open the terminal
   - Type this command and press Enter:
     ```
     pip install pycountry
     ```

## How to Use the Program

1. Open the Project
   - In VS Code, go to File → Open Folder
   - Navigate to where you saved the CopyDoc-to-Amazon folder
   - Click "Select Folder"

2. Run the Program
   - In VS Code, look for the file with a `.py` extension
   - Click to open it
   - Click the "Play" button (▶️) in the top-right corner
   OR
   - Right-click anywhere in the code
   - Select "Run Python File in Terminal"

3. Using Country Codes
   - The program uses 2-letter country codes (like "US" for United States, "GB" for United Kingdom)
   - These codes follow the ISO 3166 standard
   - Examples of common codes:
     - US = United States
     - CA = Canada
     - GB = United Kingdom
     - DE = Germany
     - FR = France
     - IT = Italy

## Troubleshooting

If you get any errors:

1. "Python is not recognized..."
   - You need to reinstall Python and make sure to check "Add Python to PATH"

2. "ModuleNotFoundError: No module named 'pycountry'"
   - Open terminal in VS Code
   - Type: `pip install pycountry`
   - Press Enter

3. Can't find the Play button
   - Make sure you have the Python extension installed
   - Make sure you're looking at a Python file (ends in .py)

## Need Help?

If you're still having trouble:
1. Take a screenshot of any error messages
2. Note what step you're stuck on
3. Contact [Your Technical Support Contact Info Here]

## Important Notes

- Always save your work before running the program
- Make sure you're using valid country codes
- The program will tell you if you enter an invalid country code

Remember: Don't worry about making mistakes - the program will guide you if something goes wrong!