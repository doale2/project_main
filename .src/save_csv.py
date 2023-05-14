from datetime import datetime
import xml.etree.ElementTree as elemTree
import pandas as pd
from ts_graph import extract_max_r2_value_ax3
from iv_fitting import iv_fitting
from iv_graph import parsing_iv_data
from sklearn.metrics import r2_score
import os


def extract_lot_data(xml):
    tree = elemTree.parse(xml)
    root = tree.getroot()  # 해당 트리의 root를 반환

    lot, wafer, mask, test, name, formatted_date, oper, row, col, analysis_wl = [], [], [], [], [], [], [], [], [], []
    for data in root.iter():
        if data.tag == 'OIOMeasurement':
            datetime_object = datetime.strptime(data.get('CreationDate'), '%a %b %d %H:%M:%S %Y')
            formatted_date = datetime_object.strftime('%Y%m%d_%H%M%S')
            oper.append(data.get('Operator'))

        elif data.tag == 'TestSiteInfo':
            lot.append(data.get('Batch'))
            test.append(data.get('TestSite'))
            wafer.append(data.get('Wafer'))
            mask.append(data.get('Maskset'))
            row.append(data.get('DieRow'))
            col.append(data.get('DieColumn'))

        elif data.tag == 'DesignParameter':
            if data.attrib.get('Name') == 'Design wavelength':
                analysis_wl.append(data.text)

        elif data.tag == 'ModulatorSite':
            name.append(data.find('Modulator').get('Name'))

    return lot, wafer, mask, test, name, formatted_date, oper, row, col, analysis_wl


def save_csv(xml):
    iv_data = parsing_iv_data(xml)
    y_fit = iv_fitting(iv_data)
    error_flag, max_f, max_r2_TS, max_transmission = extract_max_r2_value_ax3(xml)
    lot, wafer, mask, test, name, date, oper, row, col, analysis_wl = extract_lot_data(xml)

    df = pd.DataFrame({'Lot': lot, 'Wafer': wafer, 'Mask': mask, 'TestSite': test, 'Name': name, 'Date': date,
                       'Script ID': f'process {test[0].split("_")[-1]}', 'Script Version': 0.1, 'Script Owner': 'D',
                       'Operator': oper, 'Row': row, 'Column': col, 'ErrorFlag': error_flag,
                       'Error description': 'No Error' if error_flag == 0 else 'Ref. spec. Error', 'Analysis Wavelength': analysis_wl,
                       'Rsq of Ref. spectrum (Nth)': max_r2_TS, 'Max transmission of Ref. spec. (dB)': max_transmission,
                       'Rsq of IV': r2_score(iv_data['current'], y_fit), 'I at -1V [A]': iv_data['current'][4],
                       'I at 1V [A]': iv_data['current'][-1]})

    df.to_csv(f'./res/csv_files/{os.path.basename(xml)}.csv', index=False)
