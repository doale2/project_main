from tkinter import messagebox
from select_analyze_data import select_analyze_data
from iv_graph import parsing_iv_data, plot_iv, save_png_iv
from handle_subplot import handle_subplot
from ts_graph import ts_graph, ts_fitting_graph, flat_ts_graph
from save_csv import save_csv
from ts_fitting import flat_peak, plot_fitting_graph
import os
from datetime import datetime


def analyze_consequence(self, option_list):
    if self.xml_files:
        # check if all elements in the list are None
        if all([opt is None for opt in option_list]):
            messagebox.showerror("Error", "Please select at least one analysis method.")
            return
        else:
            self.progress_bar.start(100)
            analyze_data(self, option_list)
            self.progress_bar.stop()
            messagebox.showinfo("Done!", "Data analysis is complete.")
            self.progress_ratio_label.config(text="Progress ratio:  0%")
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


def function6(ax5, xml):
    flat_peak(ax5, xml)


def function7(ax6, xml):
    plot_fitting_graph(ax6, xml)


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
        ax1, ax2, ax3, ax4, ax5, ax6 = select_analyze_data(option_list)
        # data 분석할 것들을 모음
        if 'ax1' in option_list:
            ax1.set_yscale('log', base=10)
            function1(ax1, xml)
        if 'ax2' in option_list:
            function2(ax2, xml)
        if 'ax3' in option_list:
            function3(ax3, xml)
        if 'ax4' in option_list:
            function4(ax4, xml)
        if 'save_csv' in option_list:
            function5(xml, formatted_datetime)
        if 'ax5' in option_list:
            function6(ax5, xml)
            function7(ax6, xml)

        handle_subplot(ax1, ax2, ax3, ax4, ax5, ax6)
        if any(ax in option_list for ax in ['ax1', 'ax2', 'ax3', 'ax4', 'ax5']):
            save_png_iv(xml, formatted_datetime)

        self.progress_bar.step(100/len(self.xml_files))
        self.progress_ratio_label.config(text=f"Progress ratio: {round((i+1)*100/len(self.xml_files))}%")
    self.update()
