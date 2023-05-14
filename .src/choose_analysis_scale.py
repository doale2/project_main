import os
import tkinter as tk


def choose_analysis_scale(self):
    lot_set = set()
    wafer_set = set()
    coordinate_set = set()
    # dat 파일의 모든 요소에 대해 root, directories, files를 구함
    for (root, directories, files) in os.walk('./dat'):
        # file에 대해서만
        for file in files:
            if '.xml' in file: # .keep같은 파일 걸러내기
                file_split = file.split(sep='_', maxsplit=3)
                lot_set.add(file_split[0])
                wafer_set.add(file_split[1])
                coordinate_set.add(file_split[2])

    # gui에 넣기
    for lot in lot_set:
        self.select_listbox1.insert(0, lot)

    for wafer in wafer_set:
        self.select_listbox2.insert(0, wafer)

    for coordinate in coordinate_set:
        self.select_listbox3.insert(0, coordinate)

#    print(f'{lot_set}\n{wafer_set}\n{coordinate_set}')
#    selection = self.select_listbox1.get(ACTIVE)
#    print(selection)



