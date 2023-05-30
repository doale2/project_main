import os
import tkinter as tk


def choose_analysis_scale(self):
    self.choose_dict = {}
    lot_set = set()
    wafer_set = set()
    coordinate_set = set()
    date_set = set()
    # dat 파일의 모든 요소에 대해 root, directories, files를 구함
    for (root, directories, files) in os.walk('./dat'):
        # file에 대해서만
        for file in files:
            if '.xml'and 'LMZ' in file:  # .keep같은 파일 걸러내기, LMZ파일만
                file_split = file.split(sep='_', maxsplit=3)
                lot_set.add(file_split[0])
                wafer_set.add(file_split[1])
                coordinate_set.add(file_split[2])
                root_split = root.split(sep='\\')
                date_set.add(root_split[3])
                file_path = os.path.join(root, file)
                # 키:파일경로, 값:[lot, wafer, coordinate]인 dict
                self.choose_dict[file_path] = [file_split[0], file_split[1], file_split[2], root_split[3]]

    # list로 변환, 오름차순 정렬
    self.lot_list = list(lot_set)
    self.lot_list.sort()
    self.wafer_list = list(wafer_set)
    self.wafer_list.sort()
    self.coordinate_list = list(coordinate_set)
    self.coordinate_list.sort()
    self.date_list = list(date_set)
    self.date_list.sort()

    # gui에 표시하기
    for lot in self.lot_list:
        self.select_listbox1.insert(tk.END, lot)
        self.select_listbox1.configure(font=('Helvetica', 24))
    for wafer in self.wafer_list:
        self.select_listbox2.insert(tk.END, wafer)
        self.select_listbox2.configure(font=('Helvetica', 24))
    for coordinate in self.coordinate_list:
        self.select_listbox3.insert(tk.END, coordinate)
        self.select_listbox3.configure(font=('Helvetica', 24))
    for date in self.date_list:
        self.select_listbox4.insert(tk.END, date)
        self.select_listbox4.configure(font=('Helvetica', 24))
