from init_GUI import init_GUI
import customtkinter
from analyze_data import analyze_consequence
from choose_analysis_scale import choose_analysis_scale
from save_choosed_data import save_choosed_data, show_choosed_data


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        init_GUI(self)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def choose_analysis_scale(self):
        choose_analysis_scale(self)

    def save_choosed_data(self):
        save_choosed_data(self)
        show_choosed_data(self)

    def analyze_data(self, option_list):
        analyze_consequence(self, option_list)

    def exit_app(self):
        self.destroy()
