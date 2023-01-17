import os
import re
from pathlib import Path


def ReferenceMedic(folder):
    """
    ReferenceMedic is a function that will fix the references in the files in the folder.
    :param folder: the folder (your main repository folder) that contains the subdirectories and files that need to be fixed.
    :type folder: path to folder
    """
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            try:
                if filename == "reference_medic.py" or ".DS_Store" in filename:
                    continue  # skip this file
                file_path = Path(dirpath) / filename
                if file_path.suffix == ".ipynb":
                    with open(file_path, "r") as f:
                        content = f.read()
                    for file_ref in re.findall(r"\"(.+?)\"", content):
                        ref_path = Path(file_ref)
                        if ref_path.suffix == ".json":
                            new_path = "../config/" + ref_path.name
                        elif ref_path.suffix == ".csv":
                            new_path = "../config/" + ref_path.name
                        elif ref_path.suffix == ".html":
                            new_path = "../html/" + ref_path.name
                        elif ref_path.suffix == ".css":
                            new_path = "../css/" + ref_path.name
                        elif ref_path.suffix in [".jpg", ".jpeg", ".png", ".gif"]:
                            new_path = "../images/" + ref_path.name
                        elif ref_path.suffix == ".log":
                            new_path = "../logs/" + ref_path.name
                        elif ref_path.suffix == ".py":
                            new_path = "../src/" + ref_path.name
                        elif ref_path.suffix == ".txt":
                            new_path = "../txt/" + ref_path.name
                        else:
                            print(f"Invalid file type: {ref_path.suffix}, {ref_path}")
                        content = content.replace(file_ref, new_path)
                    with open(file_path, "w") as f:
                        f.write(content)
                elif file_path.suffix == ".py":
                    with open(file_path, "r") as f:
                        content = f.read()
                    for file_ref in re.findall(r"\"(.+?)\"", content):
                        ref_path = Path(file_ref)
                        if ref_path.suffix == ".json":
                            new_path = "./config/" + ref_path.name
                        elif ref_path.suffix == ".csv":
                            new_path = "./config/" + ref_path.name
                        elif ref_path.suffix == ".html":
                            new_path = "./html/" + ref_path.name
                        elif ref_path.suffix == ".css":
                            new_path = "./css/" + ref_path.name
                        elif ref_path.suffix in [".jpg", ".jpeg", ".png", ".gif"]:
                            new_path = "./images/" + ref_path.name
                        elif ref_path.suffix == ".log":
                            new_path = "./logs/" + ref_path.name
                        elif ref_path.suffix == ".py":
                            new_path = "./src/" + ref_path.name
                        elif ref_path.suffix == ".txt":
                            new_path = "./txt/" + ref_path.name
                        else:
                            print(f"Invalid file type: {ref_path.suffix}, {ref_path}")
                        content = content.replace(file_ref, new_path)
                    with open(file_path, "w") as f:
                        f.write(content)
                elif file_path.suffix == ".html":
                    with open(file_path, "r") as f:
                        content = f.read()
                    for file_ref in re.findall(r"\"(.+?)\"", content):
                        ref_path = Path(file_ref)
                        if ref_path.suffix == ".json":
                            new_path = "./config/" + ref_path.name
                        elif ref_path.suffix == ".csv":
                            new_path = "./config/" + ref_path.name
                        elif ref_path.suffix == ".html":
                            new_path = "./html/" + ref_path.name
                        elif ref_path.suffix == ".css":
                            new_path = "./css/" + ref_path.name
                        elif ref_path.suffix in [".jpg", ".jpeg", ".png", ".gif"]:
                            new_path = "./images/" + ref_path.name
                        elif ref_path.suffix == ".log":
                            new_path = "./logs/" + ref_path.name
                        elif ref_path.suffix == ".py":
                            new_path = "./src/" + ref_path.name
                        elif ref_path.suffix == ".txt":
                            new_path = "./txt/" + ref_path.name
                        else:
                            print(f"Invalid file type: {ref_path.suffix}, {ref_path}")
                        content = content.replace(file_ref, new_path)
                    with open(file_path, "w") as f:
                        f.write(content)
                elif file_path.suffix == ".css":
                    with open(file_path, "r") as f:
                        content = f.read()
                    for file_ref in re.findall(r"\"(.+?)\"", content):
                        ref_path = Path(file_ref)
                        if ref_path.suffix == ".json":
                            new_path = "./config/" + ref_path.name
                        elif ref_path.suffix == ".csv":
                            new_path = "./config/" + ref_path.name
                        elif ref_path.suffix == ".html":
                            new_path = "./html/" + ref_path.name
                        elif ref_path.suffix == ".css":
                            new_path = "./css/" + ref_path.name
                        elif ref_path.suffix in [".jpg", ".jpeg", ".png", ".gif"]:
                            new_path = "./images/" + ref_path.name
                        elif ref_path.suffix == ".log":
                            new_path = "./logs/" + ref_path.name
                        elif ref_path.suffix == ".py":
                            new_path = "./src/" + ref_path.name
                        elif ref_path.suffix == ".txt":
                            new_path = "./txt/" + ref_path.name
                        else:
                            print(f"Invalid file type: {ref_path.suffix}, {ref_path}")
                        content = content.replace(file_ref, new_path)
                    with open(file_path, "w") as f:
                        f.write(content)
                elif file_path.suffix in [".jpg", ".jpeg", ".png", ".gif"]:
                    pass
                elif file_path.suffix == ".log":
                    pass
                elif file_path.suffix == ".txt":
                    pass
                else:
                    print(f"Invalid file type: {file_path.suffix}")
                    # raise ValueError(f"Invalid file type: {file_path.suffix}")
            except Exception as e:
                print(f"Error: {e}")


def main():
    ReferenceMedic("./")  # Path to the folder containing the files to be fixed


if __name__ == "__main__":
    main()  # Run the main function
