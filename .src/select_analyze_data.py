import matplotlib.pyplot as plt


def select_analyze_data(options):
    non_empty_vars = [var for var in options if var is not None]

    # subplots 생성
    fig, axs = plt.subplots(2, 3, figsize=(18, 8))
    fig.subplots_adjust(hspace=0.5, wspace=0.5)

    # axs에 값이 있는 method_var들만 할당
    ax1, ax2, ax3, ax4 = None, None, None, None
    axs_list = []

    for i in non_empty_vars:
        if i == 'ax1':
            ax1 = axs[1][0]
            axs_list.append(ax1)
        if i == 'ax2':
            ax2 = axs[0][0]
            axs_list.append(ax2)
        if i == 'ax3':
            ax3 = axs[0][1]
            axs_list.append(ax3)
        if i == 'ax4':
            ax4 = axs[0][2]
            axs_list.append(ax4)

    # Hide other graph
    for ax in axs.flatten():
        if ax not in [ax1, ax2, ax3, ax4]:
            ax.axis('off')

    return ax1, ax2, ax3, ax4
