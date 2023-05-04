import os
from tkinter import filedialog


def set_file_path(self):
    # Get the directory path of the folder above the folder containing main.py
    main_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    # Open a file dialog to select the data folder
    folder_path = filedialog.askdirectory(
        initialdir=main_dir,
        title="Select data folder"
    )

    # Find all XML files with "LMZC" in the file name
    xml_files = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".xml") and "LMZC" in filename:
            xml_files.append(os.path.join(folder_path, filename))

    # Set the folder path and XML file paths in the GUI
    self.folder_path_var.set(folder_path)
    self.xml_file_paths_var.set(xml_files)
