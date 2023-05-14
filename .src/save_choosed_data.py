from itertools import product


def save_choosed_data(self):
    # 선택한 인덱스를 이용해서 값 구하기
    select_lot_name = []
    select_wafer_name = []
    select_coordinate_name = []
    for index in self.select_listbox1.curselection():
        select_lot_name.append(self.lot_list[index])

    for index in self.select_listbox2.curselection():
        select_wafer_name.append(self.wafer_list[index])

    for index in self.select_listbox3.curselection():
        select_coordinate_name.append(self.coordinate_list[index])

    # 선택한 값을 dat_dict에서 찾아서 키값인 path를 select_path_list 에 저장
    select_path_list = []
    product_list = list(product(*[select_lot_name, select_wafer_name, select_coordinate_name]))
    for key, value in self.choose_dict.items():
        for file_info in product_list:
            if 'LMZ' in key and self.choose_dict[key] == list(file_info):
                select_path_list.append(key)
    self.xml_files = select_path_list
