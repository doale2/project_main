import os
import tkinter as tk
from tkinter import messagebox
from select_data_folder import select_data_folder
from init_GUI import init_GUI
from clear_selected_files import clear_selected_files
from analyze_data import analyze_data


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        init_GUI(self)

    def select_data_folder(self):
        select_data_folder(self)

    def clear_selected_files(self):
        clear_selected_files(self)

    def analyze_data(self, option_list):
        analyze_data(self, option_list)

    def select_folder(self):
        folder_path = os.path.join(self.data_folder_path, self.folder_var.get())
        self.data_folder_label.config(text=f"Data Folder: {folder_path}")

    def show_selected_files(self):
        if self.xml_files:
            # If there are selected files, show the list in a message box
            file_list = "\n".join([os.path.basename(file) for file in self.xml_files])
            messagebox.showinfo("Selected Files", file_list)
        else:
            # If there are no selected files, show an error message
            messagebox.showerror("No Files Selected", "Please select data folder first.")
