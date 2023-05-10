import xml.etree.ElementTree as elemTree
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score


def parsing_ts_ref_data(xml):
    # Parse XML file
    tree = elemTree.parse(xml)
    root = tree.getroot()  # 해당 트리의 root를 반환

    for wavelength_sweep in root.iter('WavelengthSweep'):
        # Make it a dict for easier handling
        wavelength_data = {'wavelength': [], 'measured_transmission': []}
        # Get data from each element
        wavelength = list(map(float, wavelength_sweep.find('L').text.split(',')))
        measured_transmission = list(map(float, wavelength_sweep.find('IL').text.split(',')))
        wavelength_data['wavelength'].extend(wavelength)
        wavelength_data['measured_transmission'].extend(measured_transmission)

    return root, wavelength_data


def ts_graph(ax2, xml):
    root, wavelength_data = parsing_ts_ref_data(xml)

    cmap, a = plt.colormaps.get_cmap('jet'), 0
    # Extract Wavelength and dB data
    for wavelength_sweep in root.iter('WavelengthSweep'):
        # Choose a color for the scatter plot based on the iteration index
        a += 1
        color = cmap(a / 7)
        # Make it a dict for easier handling
        wavelength_data = {'wavelength': [], 'measured_transmission': []}
        # Get data from each element
        wavelength = list(map(float, wavelength_sweep.find('L').text.split(',')))
        measured_transmission = list(map(float, wavelength_sweep.find('IL').text.split(',')))
        wavelength_data['wavelength'].extend(wavelength)
        wavelength_data['measured_transmission'].extend(measured_transmission)
        # Create a scatter plot using the data
        ax2.plot('wavelength', 'measured_transmission', data=wavelength_data, color=color,
                 label=wavelength_sweep.get('DCBias') + ' V'
                 if wavelength_sweep != list(root.iter('WavelengthSweep'))[-1] else '')


def ts_fitting_graph(ax3, xml):
    import warnings
    warnings.filterwarnings('ignore', message='Polyfit may be poorly conditioned', category=np.RankWarning)
    root, wavelength_data = parsing_ts_ref_data(xml)
    cmap = plt.colormaps.get_cmap('jet')

    r2_list = []
    ax3.plot('wavelength', 'measured_transmission', data=wavelength_data, label='')
    for i in range(2, 9):
        color = cmap((i - 2) / 7)
        fp = np.polyfit(wavelength_data['wavelength'], wavelength_data['measured_transmission'], i)
        f = np.poly1d(fp)
        r2 = r2_score(wavelength_data['measured_transmission'], f(wavelength_data['wavelength']))
        r2_list.append(r2)
        ax3.plot(wavelength_data['wavelength'], f(wavelength_data['wavelength']), color=color, lw=0.8,
                 label=f'{i}th R² = {r2_list[i - 2]}')


def extract_max_r2_value_ax3(xml):
    root, wavelength_data = parsing_ts_ref_data(xml)
    r2_list = []
    max_r2 = 0

    for i in range(2, 9):
        fp = np.polyfit(wavelength_data['wavelength'], wavelength_data['measured_transmission'], i)
        f = np.poly1d(fp)
        r2 = r2_score(wavelength_data['measured_transmission'], f(wavelength_data['wavelength']))
        r2_list.append(r2)
        if r2_list[i - 2] > max_r2:
            max_f = f
            max_r2 = r2
            max_transmission = max(f(wavelength_data['wavelength']))

    if max_r2 > 0.95:
        error_flag = 0
    else:
        error_flag = 1

    return error_flag, max_f, max_r2, max_transmission


def flat_ts_graph(ax4, xml):
    import warnings
    warnings.filterwarnings('ignore', message='Polyfit may be poorly conditioned', category=np.RankWarning)
    root, wavelength_data = parsing_ts_ref_data(xml)
    error_flag, max_f, max_r2, max_transmission = extract_max_r2_value_ax3(xml)

    cmap = plt.colormaps.get_cmap('jet')
    # Iterate over the first 6 WavelengthSweep elements
    for i, wavelength_sweep in enumerate(root.iter('WavelengthSweep')):
        color = cmap(i / 7)
        flat_wavelength_data = {'wavelength': [], 'flat_measured_transmission': []}
        # Get data from each element
        wavelength = list(map(float, wavelength_sweep.find('L').text.split(',')))
        flat_measured_transmission = list(map(float, wavelength_sweep.find('IL').text.split(',')))
        flat_measured_transmission -= max_f(wavelength)
        flat_wavelength_data['wavelength'].extend(wavelength)
        flat_wavelength_data['flat_measured_transmission'].extend(flat_measured_transmission)
        # Create a scatter plot using the data
        ax4.plot('wavelength', 'flat_measured_transmission', data=flat_wavelength_data, color=color,
                 label=wavelength_sweep.get('DCBias') + ' V'
                 if wavelength_sweep != list(root.iter('WavelengthSweep'))[-1] else '')
