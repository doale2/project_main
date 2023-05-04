import tkinter as tk
from tkinter import ttk


def init_GUI(self):
    self.title("Wafer Analysis")
    self.geometry("400x300")

    self.data_folder_label = tk.Label(self, text="Data Folder: ")
    self.data_folder_label.grid(row=0, column=0, sticky="w")

    self.data_folder_listbox = tk.Listbox(self, width=30)
    self.data_folder_listbox.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

    self.set_data_folder_button = tk.Button(self, text="Set Data Folder", command=self.select_data_folder)
    self.set_data_folder_button.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    self.num_files_label = tk.Label(self, text="Number of Files: 0")
    self.num_files_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

    self.show_selected_files_button = tk.Button(self, text="Show Selected Files", command=self.show_selected_files)
    self.show_selected_files_button.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    self.clear_selected_files_button = tk.Button(self, text="Clear Files", command=self.clear_selected_files)
    self.clear_selected_files_button.grid(row=3, column=0, padx=5, pady=5, sticky="e")

    self.analyze_button = tk.Button(self, text="Analyze", command=self.analyze_data)
    self.analyze_button.grid(row=5, column=0, padx=5, pady=5, sticky="w")

    self.xml_files = []

    self.folder_var = tk.StringVar(self)
    self.folder_select = ttk.Combobox(self, textvariable=self.folder_var, state='readonly')
    self.folder_select.bind('<<ComboboxSelected>>', self.select_folder)
