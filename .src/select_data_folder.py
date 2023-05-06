import os
import tkinter as tk
from tkinter import filedialog
from select_xml import select_lmz_files


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
        self.xml_files += select_lmz_files(subdir_path)

    # Store path in the class variables
    self.data_folder_path = data_folder_path

    # Update the GUI labels with the selected path and number of files
    self.data_folder_label.config(text=f"Data Folder: {data_folder_path}")
    self.num_files_label.config(text=f"Number of Files: {len(self.xml_files)}")
