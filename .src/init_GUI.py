import tkinter as tk
from tkinter import ttk


def init_GUI(self):
    method_var1 = tk.IntVar()
    method_var2 = tk.IntVar()
    method_var3 = tk.IntVar()
    method_var4 = tk.IntVar()
    method_var5 = tk.IntVar()

    self.title("Wafer Analysis")
    self.geometry("380x600")

    self.data_folder_label = tk.Label(self, text="Data Folder: ")
    self.data_folder_label.grid(row=0, column=0, sticky="w")

    self.data_folder_listbox = tk.Listbox(self, width=52)
    self.data_folder_listbox.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

    self.set_data_folder_button = tk.Button(self, text="Set Data Folder", command=self.select_data_folder)
    self.set_data_folder_button.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    self.num_files_label = tk.Label(self, text="Number of Files: 0")
    self.num_files_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

    self.show_selected_files_button = tk.Button(self, text="Show Selected Files", command=self.show_selected_files)
    self.show_selected_files_button.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    self.clear_selected_files_button = tk.Button(self, text="Clear Files", command=self.clear_selected_files)
    self.clear_selected_files_button.grid(row=3, column=0, padx=5, pady=5, sticky="e")

    self.progress_ratio_label = tk.Label(self, text="Progress ratio:  0%")
    self.progress_ratio_label.grid(row=5, column=0, sticky="e")

    self.progress_bar = ttk.Progressbar(self, length=110,orient="horizontal", mode="determinate")
    self.progress_bar.grid(row=6, column=0, sticky="e")
    self.analyze_button = tk.Button(self, text="Analyze", command=lambda: self.analyze_data([
        'ax1' if method_var1.get() else None,
        'ax2' if method_var2.get() else None,
        'ax3' if method_var3.get() else None,
        'ax4' if method_var4.get() else None,
        'save_csv' if method_var5.get() else None
    ]))
    self.analyze_button.grid(row=5, column=0, padx=5, pady=5, sticky="w")

    self.xml_files = []

    self.folder_var = tk.StringVar(self)
    self.folder_select = ttk.Combobox(self, textvariable=self.folder_var, state='readonly')
    self.folder_select.bind('<<ComboboxSelected>>', self.select_folder)

    self.toggle_button = tk.Checkbutton(self, text="method1", padx=20, variable=method_var1)
    self.toggle_button.grid(row=6, column=0, padx=5, pady=5, sticky="w")

    self.toggle_button2 = tk.Checkbutton(self, text="method2", padx=20, variable=method_var2)
    self.toggle_button2.grid(row=7, column=0, padx=5, pady=5, sticky="w")

    self.toggle_button3 = tk.Checkbutton(self,text="method3", padx=20, variable=method_var3)
    self.toggle_button3.grid(row=8, column=0, padx=5, pady=5, sticky="w")

    self.toggle_button4 = tk.Checkbutton(self,text="method4", padx=20, variable=method_var4)
    self.toggle_button4.grid(row=9, column=0, padx=5, pady=5, sticky="w")

    self.toggle_button5 = tk.Checkbutton(self,text="save_csv", padx=20, variable=method_var5)
    self.toggle_button5.grid(row=10, column=0, padx=5, pady=5, sticky="w")
