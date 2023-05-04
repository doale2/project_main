import os
import tkinter as tk
from tkinter import filedialog
from select_xml import select_lmzc_files


# ver1
def select_data_folder(self):
    # Select the data folder
    data_folder_path = filedialog.askdirectory(initialdir=os.path.join(os.getcwd(), "../dat"), title="Select XML file",
                                               parent=self)
    if data_folder_path:
        self.data_folder_label.config(text=f"Data Folder: {data_folder_path}")

    # Get the subdirectories in the data folder
    subdirectories = [f for f in os.listdir(data_folder_path) if os.path.isdir(os.path.join(data_folder_path, f))]

    # Add the subdirectories to the listbox
    for subdir in subdirectories:
        self.data_folder_listbox.insert(tk.END, subdir)

    # Otherwise, open a file dialog window to select the data folder
    if not data_folder_path:
        return  # Cancelled

    # Select LMZC XML files in the selected data folder and all subdirectories
    for subdir in subdirectories:
        subdir_path = os.path.join(data_folder_path, subdir)
        self.xml_files += select_lmzc_files(subdir_path)

    # Store path in the class variables
    self.data_folder_path = data_folder_path

    # Update the GUI labels with the selected path and number of files
    self.data_folder_label.config(text=f"Data Folder: {data_folder_path}")
    self.num_files_label.config(text=f"Number of Files: {len(self.xml_files)}")

# ver2
# def select_data_folder(self):
#     # Select the data folders
#     data_folder_paths = filedialog.askopenfilenames(initialdir=os.path.join(os.getcwd(), "../dat"),
#                                                     title="Select Data Folders", parent=self,
#                                                     filetypes=[("Directory", "*")])
#
#     if not data_folder_paths:
#         return []  # Cancelled
#
#     # Find all subdirectories in the selected data folders
#     subdirectories = []
#     for folder_path in data_folder_paths:
#         for dirpath, dirnames, filenames in os.walk(folder_path):
#             for dirname in dirnames:
#                 subdirectories.append(os.path.join(dirpath, dirname))
#
#     # Combine selected directories and all subdirectories
#     data_folders = list(data_folder_paths) + subdirectories
#
#     return data_folders
