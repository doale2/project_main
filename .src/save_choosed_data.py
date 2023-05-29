import os
from itertools import product
from tkinter import messagebox
import customtkinter


def save_choosed_data(self):
    # 선택한 인덱스를 이용해서 값 구하기
    select_lot_name = []
    select_wafer_name = []
    select_coordinate_name = []
    select_date_name = []

    # 선택한 것을 추가, 아무것도 선택하지 않으면 전체선택
    if self.select_listbox1.curselection() == ():
        select_lot_name = self.lot_list
    else:
        for index in self.select_listbox1.curselection():
            select_lot_name.append(self.lot_list[index])

    if self.select_listbox2.curselection() == ():
        select_wafer_name = self.wafer_list
    else:
        for index in self.select_listbox2.curselection():
            select_wafer_name.append(self.wafer_list[index])

    if self.select_listbox3.curselection() == ():
        select_coordinate_name = self.coordinate_list
    else:
        for index in self.select_listbox3.curselection():
            select_coordinate_name.append(self.coordinate_list[index])

    if self.select_listbox4.curselection() == ():
        select_date_name = self.date_list
    else:
        for index in self.select_listbox4.curselection():
            select_date_name.append(self.date_list[index])

    # 선택한 값을 dat_dict에서 찾아서 키값인 path를 select_path_list 에 저장
    select_path_list = []
    product_list = list(product(*[select_lot_name, select_wafer_name, select_coordinate_name, select_date_name]))
    for key, value in self.choose_dict.items():
        for file_info in product_list:
            if 'LMZ' in key and self.choose_dict[key] == list(file_info):
                select_path_list.append(key)
    self.xml_files = select_path_list

    self.num_files_label.configure(text=f"Number of Files: {len(self.xml_files)}")
    if len(self.xml_files) == 0:
        messagebox.showerror("Error", 'Please select XML files again')


def show_choosed_data(self):
    self.textbox.configure(state='normal')
    self.textbox.delete(1.0, customtkinter.END)
    # Display selected xml file names
    for xml_file in self.xml_files:
        file_name = os.path.basename(xml_file)  # 파일 경로에서 파일 이름만 추출
        self.textbox.insert(customtkinter.END, file_name + "\n")
    self.textbox.configure(state='disabled')
