import numpy as np
from lmfit import Model
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
from ts_graph import parsing_ts_ref_data, extract_max_r2_value_ax3


def dbm_to_linear(dBm):
    linear = 10 ** (dBm/10)
    return linear


def flat_peak(ax5, xml):
    import warnings
    warnings.filterwarnings('ignore', message='Polyfit may be poorly conditioned', category=np.RankWarning)
    root, wavelength_data = parsing_ts_ref_data(xml)
    error_flag, max_f, max_r2, max_transmission = extract_max_r2_value_ax3(xml)
    cmap = plt.colormaps.get_cmap('jet')

    for i, wavelength_sweep in enumerate(root.iter('WavelengthSweep')):
        if i != 6:
            color = cmap(i / 6)
            # Make it a dict for easier handling
            wavelength_data = {'wavelength': [], 'measured_transmission': []}
            # Get data from each element
            wavelength = list(map(float, wavelength_sweep.find('L').text.split(',')))
            measured_transmission = list(map(float, wavelength_sweep.find('IL').text.split(',')))
            # Subtract y2
            measured_transmission -= max_f(wavelength)
            wavelength_data['wavelength'].extend(wavelength)
            wavelength_data['measured_transmission'].extend(measured_transmission)
            # Extract peak
            peaks_index, _ = find_peaks(wavelength_data['measured_transmission'], prominence=5)
            x_peaks, y_peaks = [], []
            for index in peaks_index:
                x_peaks.append(wavelength_data['wavelength'][index])
                y_peaks.append(wavelength_data['measured_transmission'][index])

            fp = np.polyfit(x_peaks, y_peaks, 1)  # 극댓값들로 1차 근사
            f = np.poly1d(fp)  # Equation으로 만듬

            wavelength_data['measured_transmission'] -= f(wavelength)
            wavelength_data['measured_transmission'] = dbm_to_linear(wavelength_data['measured_transmission'])
            ax5.plot('wavelength', 'measured_transmission', data=wavelength_data, color=color,
                     label=wavelength_sweep.get('DCBias') + ' V')


def plot_fitting_graph(ax6, xml):
    import warnings
    warnings.filterwarnings('ignore', message='Polyfit may be poorly conditioned', category=np.RankWarning)
    root, wavelength_data = parsing_ts_ref_data(xml)
    error_flag, max_f, max_r2, max_transmission = extract_max_r2_value_ax3(xml)
    cmap = plt.colormaps.get_cmap('jet')

    for i, wavelength_sweep in enumerate(root.iter('WavelengthSweep')):
        if i == 4:
            color = cmap(i / 6)
            # Make it a dict for easier handling
            wavelength_data = {'wavelength': [], 'measured_transmission': []}
            # Get data from each element
            wavelength = list(map(float, wavelength_sweep.find('L').text.split(',')))
            measured_transmission = list(map(float, wavelength_sweep.find('IL').text.split(',')))
            # Subtract y2
            measured_transmission -= max_f(wavelength)
            wavelength_data['wavelength'].extend(wavelength)
            wavelength_data['measured_transmission'].extend(measured_transmission)
            # Extract peak
            peaks_index, _ = find_peaks(wavelength_data['measured_transmission'], prominence=5)
            x_peaks, y_peaks = [], []
            for index in peaks_index:
                x_peaks.append(wavelength_data['wavelength'][index])
                y_peaks.append(wavelength_data['measured_transmission'][index])

            fp = np.polyfit(x_peaks, y_peaks, 1)  # 극댓값들로 1차 근사
            f = np.poly1d(fp)  # Equation으로 만듬

            wavelength_data['measured_transmission'] -= f(wavelength)
            wavelength_data['measured_transmission'] = dbm_to_linear(wavelength_data['measured_transmission'])
            ax6.plot('wavelength', 'measured_transmission', data=wavelength_data, color=color, lw=1,
                     label=wavelength_sweep.get('DCBias') + ' V')

            model = Model(fitting_extract_n_eff, independent_vars=['wavelength'], param_names=['I_0', 'n_eff'])

            # Set the initial parameter values and boundaries
            model.set_param_hint('I_0', value=0.5, min=-1.0, max=1.0)
            model.set_param_hint('n_eff', value=2.6, min=0.0, max=10.0)

            # Fit the model to the data
            result = model.fit(wavelength_data['measured_transmission'], wavelength=wavelength)
            ax6.plot(wavelength_data['wavelength'], result.best_fit, linestyle='-', lw=2, color='aqua',
                     label=wavelength_sweep.get('DCBias') + 'best-fit')
            print(result.best_values)


def fitting_extract_n_eff(wavelength, I_0, n_eff):
    return I_0 * (np.sin(np.pi * 40 * n_eff / wavelength)) ** 2


# def fitting_y3(I_0, wavelength, l, n_eff, del_n_eff):
#      return I_0 * (np.sin(np.pi / wavelength * (40 * n_eff + l * del_n_eff))) ** 2


# # Approach the path
# rootDir = "C:/Users/노정완/Desktop/대학교/23나노 1학기 PDF/공학프로그래밍2/data set/"  # Input your path
# fname = 'HY202103_D07_(0,0)_LION1_DCM_LMZC.xml'  # Input file name
# xml = rootDir + fname
