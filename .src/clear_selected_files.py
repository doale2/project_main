import tkinter as tk


def clear_selected_files(self):
    self.data_folder_listbox.delete(0, tk.END)
    self.xml_files = []
    self.num_files_label.config(text=f"Number of Files: 0")

