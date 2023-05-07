def handle_subplot(ax1, ax2, ax3, ax4):
    # Setting details
    detail_list = [
        {'ax1_title': 'IV - analysis', 'ax1_titlesize': 11,
         'ax1_xlabel': 'Voltage [V]', 'ax1_ylabel': 'Current [A]', 'ax1_size': 9, 'ax1_ticksize': 14,
         'ax1_legendloc': 'best', 'ax1_legendncol': 1, 'ax1_legendsize': 10},

        {'ax2_title': 'Transmission spectra - as measured', 'ax2_titlesize': 11,
         'ax2_xlabel': 'Wavelength [nm]', 'ax2_ylabel': 'Measured_transmission [dB]', 'ax2_size': 9, 'ax2_ticksize': 14,
         'ax2_legendloc': 'lower center', 'ax2_legendncol': 3, 'ax2_legendsize': 8},

        {'ax3_title': 'Transmission spectra - as measured', 'ax3_titlesize': 11,
         'ax3_xlabel': 'Wavelength [nm]', 'ax3_ylabel': 'Fitting Reference data', 'ax3_size': 9, 'ax3_ticksize': 14,
         'ax3_legendloc': 'lower center', 'ax3_legendncol': 1, 'ax3_legendsize': 6.5},

        {'ax4_title': 'Flat Transmission spectra - as measured', 'ax4_titlesize': 11,
         'ax4_xlabel': 'Wavelength [nm]', 'ax4_ylabel': 'Flat Measured_transmission [dB]', 'ax4_size': 9,
         'ax4_ticksize': 14,
         'ax4_legendloc': 'lower center', 'ax4_legendncol': 3, 'ax4_legendsize': 8}
    ]

    for i, axs in enumerate([ax1, ax2, ax3, ax4]):
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
