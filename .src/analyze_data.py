from tkinter import messagebox
from matplotlib import pyplot as plt
from iv_graph import parsing_iv_data, plot_iv, save_png_iv
from setting_subplots import setting_subplots, handle_subplot
from ts_graph import ts_graph, ts_fitting_graph, flat_ts_graph
from save_csv import save_csv
from ts_fitting import flat_peak_fitting
import os
from datetime import datetime


def analyze_consequence(self, option_list):
    if self.xml_files:
        # check if all elements in the list are None
        if all([opt is None for opt in option_list]):
            messagebox.showerror("Error", "Please select at least one analysis method.")
            return
        else:
            analyze_data(self, option_list)
            messagebox.showinfo("Done!", "Data analysis is complete.")
            self.progress_ratio_label.configure(text="Progress ratio:  0%")
    else:
        messagebox.showerror("Error", "please select at least one xml files")


def show_selected_files(self):
    if self.xml_files:
        # If there are selected files, show the list in a message box
        file_list = "\n".join([os.path.basename(file) for file in self.xml_files])
        messagebox.showinfo("Selected Files", file_list)
    else:
        # If there are no selected files, show an error message
        messagebox.showerror("No Files Selected", "Please select data folder first.")


def function1(ax1, xml):
    plot_iv(ax1, parsing_iv_data(xml))


def function2(ax2, xml):
    ts_graph(ax2, xml)


def function3(ax3, xml):
    ts_fitting_graph(ax3, xml)


def function4(ax4, xml):
    flat_ts_graph(ax4, xml)

def function5(xml, formatted_datetime):
    save_csv(xml, formatted_datetime)

def function6(ax5, ax6, xml):
    flat_peak_fitting(ax5, ax6, xml)
    if "LMZC" in xml:
        ax5.set_xlim(1547, 1553)  # X축 범위 설정
    else:
        ax5.set_xlim(1307, 1313)  # X축 범위 설정
def create_res_subfolders():
    # 분석 시간 폴더 생성
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y.%m.%d-%H%M%S")
    for root, dirs, files in os.walk('./dat'):
        if os.path.basename(root) != 'dat':
            for folder in dirs:
                folder_path = os.path.join(root, folder)
                res_folder_path = os.path.join(f'./res/{formatted_datetime}', os.path.relpath(folder_path, './dat'))
                os.makedirs(res_folder_path, exist_ok=True)
    return formatted_datetime


def analyze_data(self, option_list):
    formatted_datetime = create_res_subfolders()
    for i, xml in enumerate(self.xml_files):
        self.update()
        ax1, ax2, ax3, ax4, ax5, ax6 = setting_subplots()
        # data 분석
        if 'csv' in option_list:
            function5(xml, formatted_datetime)
        if 'png' in option_list:
            ax1.set_yscale('log', base=10)
            function1(ax1, xml)
            function2(ax2, xml)
            function3(ax3, xml)
            function4(ax4, xml)
            function6(ax5, ax6, xml)
            handle_subplot(ax1, ax2, ax3, ax4, ax5, ax6)
            save_png_iv(xml, formatted_datetime)

        plt.close('all')
        self.progress_value.set((i + 1) / len(self.xml_files))
        self.progress_bar.update_idletasks()
        self.progress_ratio_label.configure(text=f"Progress ratio: {round(100* self.progress_value.get(), 2)}%")
    self.update()
