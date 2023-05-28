import tkinter as tk
from init_GUI import init_GUI
from clear_selected_files import clear_selected_files
from analyze_data import analyze_consequence, show_selected_files
from choose_analysis_scale import choose_analysis_scale
from save_choosed_data import save_choosed_data


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        init_GUI(self)

    def choose_analysis_scale(self):
        choose_analysis_scale(self)

    def save_choosed_data(self):
        save_choosed_data(self)

    def clear_selected_files(self):
        clear_selected_files(self)

    def analyze_data(self, option_list):
        analyze_consequence(self, option_list)

    def show_selected_files(self):
        show_selected_files(self)
