import matplotlib.pyplot as plt


def setting_subplots():
    # subplots 생성
    fig, axs = plt.subplots(3, 3, figsize=(18, 10.125))
    fig.subplots_adjust(hspace=0.7, wspace=0.5)

    ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8 = axs[1][0], axs[0][0], axs[0][1], axs[0][2], axs[1][1], axs[2][0], axs[1][2], axs[2][1]
    # Hide other graph
    for ax in axs.flatten():
        if ax not in [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8]:
            ax.axis('off')

    return ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8


def handle_subplot(ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8):
    # Setting details
    detail_list = [
        {'ax1_title': 'IV - analysis', 'ax1_titlesize': 11,
         'ax1_xlabel': 'Voltage [V]', 'ax1_ylabel': 'Current [A]', 'ax1_size': 9, 'ax1_ticksize': 14,
         'ax1_legendloc': 'lower center', 'ax1_legendncol': 1, 'ax1_legendsize': 10},

        {'ax2_title': 'Transmission spectra - as measured', 'ax2_titlesize': 11,
         'ax2_xlabel': 'Wavelength [nm]', 'ax2_ylabel': 'Measured_transmission [dBm]', 'ax2_size': 9, 'ax2_ticksize': 14,
         'ax2_legendloc': 'lower center', 'ax2_legendncol': 3, 'ax2_legendsize': 8},

        {'ax3_title': 'Transmission spectra - as measured', 'ax3_titlesize': 11,
         'ax3_xlabel': 'Wavelength [nm]', 'ax3_ylabel': 'Fitting Reference data [dBm]', 'ax3_size': 9, 'ax3_ticksize': 14,
         'ax3_legendloc': 'lower center', 'ax3_legendncol': 1, 'ax3_legendsize': 6.5},

        {'ax4_title': 'Flat Transmission spectra - as measured', 'ax4_titlesize': 11,
         'ax4_xlabel': 'Wavelength [nm]', 'ax4_ylabel': 'Flat Measured_transmission [dBm]', 'ax4_size': 9,
         'ax4_ticksize': 14,
         'ax4_legendloc': 'lower center', 'ax4_legendncol': 3, 'ax4_legendsize': 6},

        {'ax5_title': 'Flat Flat TS', 'ax5_titlesize': 11,
         'ax5_xlabel': 'Wavelength [nm]', 'ax5_ylabel': 'Intensity [a.u.]', 'ax5_size': 9,
         'ax5_ticksize': 14,
         'ax5_legendloc': 'lower center', 'ax5_legendncol': 3, 'ax5_legendsize': 6},

        {'ax6_title': 'n_V_curve', 'ax6_titlesize': 11,
         'ax6_xlabel': 'Voltage [V]', 'ax6_ylabel': 'del_n_eff', 'ax6_size': 9,
         'ax6_ticksize': 14,
         'ax6_legendloc': 'lower center', 'ax6_legendncol': 1, 'ax6_legendsize': 8},

        {'ax7_title': 'Flat Flat TS Enlarged', 'ax7_titlesize': 11,
         'ax7_xlabel': 'Wavelength [nm]', 'ax7_ylabel': 'Intensity [a.u.]', 'ax7_size': 9,
         'ax7_ticksize': 14,
         'ax7_legendloc': 'upper center', 'ax7_legendncol': 3, 'ax7_legendsize': 4},

        {'ax8_title': 'Flat Flat TS Enlarged dBm', 'ax8_titlesize': 11,
         'ax8_xlabel': 'Wavelength [nm]', 'ax8_ylabel': 'Flat Measured_transmission [dBm]', 'ax8_size': 9,
         'ax8_ticksize': 14,
         'ax8_legendloc': 'lower right', 'ax8_legendncol': 1, 'ax8_legendsize': 4}
    ]

    for i, axs in enumerate([ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8]):
        if axs is not None:
            details = detail_list[i]
            axs.set_xlabel(details[f'ax{i + 1}_xlabel'], size=details[f'ax{i + 1}_size'], fontweight='bold')
            axs.set_ylabel(details[f'ax{i + 1}_ylabel'], size=details[f'ax{i + 1}_size'], fontweight='bold')
            axs.set_title(details[f'ax{i + 1}_title'], size=details[f'ax{i + 1}_titlesize'], fontweight='bold',
                          style='italic')
            axs.tick_params(axis='both', which='major', size=details[f'ax{i + 1}_legendsize'])  # tick 크기 설정
            axs.legend(loc=details[f'ax{i + 1}_legendloc'], ncol=details[f'ax{i + 1}_legendncol'],
                       fontsize=details[f'ax{i + 1}_legendsize'])
            axs.grid()
