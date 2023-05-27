import matplotlib.pyplot as plt


def select_analyze_data():
    # subplots 생성
    fig, axs = plt.subplots(2, 3, figsize=(18, 8))
    fig.subplots_adjust(hspace=0.5, wspace=0.5)

    ax1, ax2, ax3, ax4, ax5, ax6 = axs[1][0], axs[0][0], axs[0][1], axs[0][2], axs[1][1], axs[1][2]

    return ax1, ax2, ax3, ax4, ax5, ax6
