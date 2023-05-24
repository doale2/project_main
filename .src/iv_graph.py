import xml.etree.ElementTree as elemTree
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from iv_fitting import iv_fitting
import os


def parsing_iv_data(xml):
    # Parse XML file
    tree = elemTree.parse(xml)
    root = tree.getroot()  # 해당 트리의 root를 반환

    iv_data = {'voltage': [], 'current': []}
    for iv_measurement in root.iter('IVMeasurement'):
        current = list(map(float, iv_measurement.find('Current').text.split(',')))
        voltage = list(map(float, iv_measurement.find('Voltage').text.split(',')))
        current_abs = [abs(i) for i in current]
        iv_data['voltage'].extend(voltage)
        iv_data['current'].extend(current_abs)

    return iv_data


def plot_iv(ax1, iv_data):
    # Plot data using matplotlib
    ax1.scatter('voltage', 'current', data=iv_data, color='mediumseagreen', label='data')
    ax1.plot(iv_data['voltage'], iv_fitting(iv_data), linestyle='--', lw=2, color='r', label='best-fit')
    # Add annotations for current values and R-squared value
    for x, y in zip(iv_data['voltage'], iv_data['current']):
        if x in [-2.0, -1.0, 1.0]:
            ax1.annotate(f"{y:.2e}A", xy=(x, y), xytext=(3, 10), textcoords='offset points', ha='center', fontsize=8)
    ax1.annotate(f"R² = {r2_score(iv_data['current'], iv_fitting(iv_data))}", xy=(-2.1, 10 ** -6), ha='left',
                 fontsize=9)


def save_png_iv(xml, formatted_datetime):
    # 파일 경로 추출하여 저장
    directory_path = os.path.dirname(xml)
    directory_path = directory_path.replace("\\", "/")
    directory_path = directory_path.replace("./dat", "")
    save_directory = f'./res/{formatted_datetime}/{directory_path}'
    # 파일 명만 가져옴
    filename = os.path.basename(xml)
    filename = os.path.splitext(filename)[0]
    plt.savefig(f'{save_directory}/{filename}.png', dpi=300)
