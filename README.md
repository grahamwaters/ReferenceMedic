# Reference Medic
Are you tired of manually updating file references in your project? Look no further than Reference Medic! This tool scans your project's files and updates any file references to adhere to your specified file structure.

# Getting Started
To use Reference Medic, simply run the script and provide the top-level folder of your project as the argument. The script will then recursively scan through all subfolders and update any file references as necessary.

ReferenceMedic("path/to/project_folder")
File Structure Rules
Reference Medic currently supports the following file structure rules:

## For Jupyter Notebooks
- If the file being referenced is a .json file, the relative path will be changed to ../config/{filename}
- If the file being referenced is a .csv file, the relative path will be changed to ../config/{filename}
- .html files are now stored in the ../html folder
- .css files are in the ../css folder
- Any image files (.jpg, .jpeg, .png, .gif) are now in the ../images folder
- .log files are in the ../logs folder
- .py files are now in ../src
- .txt files are in ../txt
## For Python Scripts
- If the file being referenced is a .json file, the relative path will be changed to ./config/{filename}
- If the file being referenced is a .csv file, the relative path will be changed to ./config/{filename}
- .html files are now stored in the ./html folder
- .css files are in the ./css folder
- Any image files (.jpg, .jpeg, .png, .gif) are now in the ./images folder
- .log files are in the ./logs folder
- .py files are now in ./src
- .txt files are in ./txt
- Any other file types will raise an error.

# Before Reference Medic
```python
with open("ppn_deck.json", "r") as read_file:
    card_deck = json.load(read_file)
```

# After Reference Medic
```python
with open("../config/ppn_deck.json", "r") as read_file:
    card_deck = json.load(read_file)
```
# Additional Features
You can also customize the script to your own file structure rules by editing the code.

# Built With
* Python
* Jupyter Notebook
* Visual Studio Code
* os
* pathlib
* json
* re

# Authors
* **Graham Waters** - [grahamwaters](https://github.com/grahamwaters)

# License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
