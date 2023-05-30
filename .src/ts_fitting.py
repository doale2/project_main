import math
import numpy as np
from lmfit import Model
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
from ts_graph import parsing_ts_ref_data, extract_max_r2_value_ax3


def dbm_to_linear(dBm):
    linear = 10 ** (dBm / 10) / 1000
    return linear


def linear_to_dBm(linear):
    dBm = 10 * math.log10(linear * 1000)
    return dBm


def fitting_extract_n_eff(wavelength, n_eff):
    I_0 = 0.001
    subtraction_l2_l1 = 40000
    return I_0 * (np.sin(np.pi * subtraction_l2_l1 * n_eff / wavelength)) ** 2


def extract_n_eff(xml):
    import warnings
    warnings.filterwarnings('ignore', message='Polyfit may be poorly conditioned', category=np.RankWarning)
    root, wavelength_data = parsing_ts_ref_data(xml)
    max_i, error_flag, max_f, max_r2, max_transmission = extract_max_r2_value_ax3(xml)

    for i, wavelength_sweep in enumerate(root.iter('WavelengthSweep')):
        if i == 4:
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
            peaks_index, _ = find_peaks(wavelength_data['measured_transmission'], prominence=6)
            x_peaks, y_peaks = [], []
            for index in peaks_index:
                x_peaks.append(wavelength_data['wavelength'][index])
                y_peaks.append(wavelength_data['measured_transmission'][index])

            fp = np.polyfit(x_peaks, y_peaks, 1)  # 극댓값들로 1차 근사
            f = np.poly1d(fp)  # Equation으로 만듬

            wavelength_data['measured_transmission'] -= f(wavelength)
            wavelength_data['measured_transmission'] = dbm_to_linear(wavelength_data['measured_transmission'])
            # Fitting 0V for extracting n_eff
            model = Model(fitting_extract_n_eff, independent_vars=['wavelength'], param_names=['n_eff'])

            # Set the initial parameter values and boundaries
            model.set_param_hint('n_eff', value=4.2, min=0.0, max=10.0)

            # Fit the model to the data
            result = model.fit(wavelength_data['measured_transmission'], wavelength=wavelength)
            return result.best_values.get('n_eff')


def fitting_consider_voltage(wavelength, n_eff_0, del_n_eff):
    I_0 = 0.001
    l = 500000
    subtraction_l2_l1 = 40000
    return I_0 * (np.sin(np.pi / wavelength * (subtraction_l2_l1 * n_eff_0 + l * del_n_eff))) ** 2


def flat_peak_fitting(ax5, ax6, ax7, ax8, xml):
    import warnings
    warnings.filterwarnings('ignore', message='Polyfit may be poorly conditioned', category=np.RankWarning)
    root, wavelength_data = parsing_ts_ref_data(xml)
    max_i, error_flag, max_f, max_r2, max_transmission = extract_max_r2_value_ax3(xml)
    cmap = plt.colormaps.get_cmap('jet')
    del_n_list, v_list = [], []
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
            ax5.scatter('wavelength', 'measured_transmission', data=wavelength_data, color=color, s=0.01, alpha=0.9,
                        label=wavelength_sweep.get('DCBias') + ' V')
            ax7.scatter('wavelength', 'measured_transmission', data=wavelength_data, color=color, s=0.01, alpha=0.9,
                        label=wavelength_sweep.get('DCBias') + ' V')
            y_dBm = [linear_to_dBm(y) for y in wavelength_data['measured_transmission']]
            ax8.scatter(wavelength, y_dBm, color=color, s=0.01, alpha=0.9,
                        label=wavelength_sweep.get('DCBias') + ' V')
            model = Model(fitting_consider_voltage, independent_vars=['wavelength'],
                          param_names=['n_eff_0', 'del_n_eff'])

            # Set the initial parameter values and boundaries
            model.set_param_hint('n_eff_0', value=extract_n_eff(xml), vary=False)
            model.set_param_hint('del_n_eff', value=0.0)

            # Fit the model to the data
            result = model.fit(wavelength_data['measured_transmission'], wavelength=wavelength)
            del_n_list.append(result.best_values.get('del_n_eff'))
            v_list.append(wavelength_sweep.get('DCBias'))
            ax5.plot(wavelength, result.best_fit, color=color, linestyle=':',
                     label=wavelength_sweep.get('DCBias') + ' V fit', lw=1)
            ax7.plot(wavelength, result.best_fit, color=color, linestyle=':',
                     label=wavelength_sweep.get('DCBias') + ' V fit', lw=1)
            result_dBm = [linear_to_dBm(result) for result in result.best_fit]
            ax8.plot(wavelength, result_dBm, color=color, linestyle=':',
                     label=wavelength_sweep.get('DCBias') + ' V fit', lw=1)

            # Find the index of the closest value to the desired x position
            if "LMZC" in xml:
                reference_x = 1550
            else:
                reference_x = 1310

            # Find the local minima indices in measured_transmission
            local_minima_indices = []
            for j in range(1, len(wavelength) - 1):
                if result_dBm[j] < result_dBm[j - 1] and result_dBm[j] < result_dBm[j + 1]:
                    local_minima_indices.append(j)

            # Find the index of the local minimum closest to the reference x-coordinate
            closest_index = min(local_minima_indices, key=lambda k: abs(wavelength[k] - reference_x))

            # Set the x-axis range for zooming in around the reference value
            zoom_range = 5
            zoom_start = max(wavelength[closest_index] - zoom_range, wavelength[0])
            zoom_end = min(wavelength[closest_index] + zoom_range, wavelength[-1])
            ax7.set_xlim(zoom_start, zoom_end)
            ax8.set_xlim(zoom_start, zoom_end)

    v_list = list(map(float, v_list))
    del_n_list = list(map(float, del_n_list))
    ax6.scatter(v_list, del_n_list, label='n_V_curve')
    fp_ax6 = np.polyfit(v_list, del_n_list, 2)  # 2차 근사
    f = np.poly1d(fp_ax6)  # Equation으로 만듬
    ax6.plot(v_list, list(f(v_list)), color='r', linestyle='--', lw=1, label='2th n_V fit')
    # VpiL 구하기
    try:
        if "LMZC" in xml:
            VpiL = 1550e-7 / (del_n_list[0] - del_n_list[-2])
        else:
            VpiL = 1310e-7 / (del_n_list[0] - del_n_list[-2])
    except ZeroDivisionError:
        VpiL = 'Cannot calculate VpiL'

    ax6.annotate(f'VpiL: {VpiL} [V·cm]', xy=(1, 1), xycoords='axes fraction', xytext=(0.95, 0.95),
                 textcoords='axes fraction', fontsize=9, ha='right', va='top',
                 bbox=dict(boxstyle='round', facecolor='white', edgecolor='gray'))
