from select_analyze_data import select_analyze_data
from iv_graph import parsing_iv_data, plot_iv, save_png_iv
from handle_subplot import handle_subplot
from ts_graph import ts_graph, ts_fitting_graph, flat_ts_graph
from save_csv import save_csv


def function1(ax1, xml):
    plot_iv(ax1, parsing_iv_data(xml))


def function2(ax2, xml):
    ts_graph(ax2, xml)


def function3(ax3, xml):
    ts_fitting_graph(ax3, xml)


def function4(ax4, xml):
    flat_ts_graph(ax4, xml)


def function5(xml):
    save_csv(xml)


def analyze_data(self, option_list):
    print(option_list)
    for xml in self.xml_files:
        ax1, ax2, ax3, ax4 = select_analyze_data(option_list)

        # data 분석할 것들을 모음
        if 'ax1' in option_list:
            ax1.set_yscale('log', base=10)
            function1(ax1, xml)
        if 'ax2' in option_list:
            function2(ax2, xml)
        if 'ax3' in option_list:
            function3(ax3, xml)
        if 'ax4' in option_list:
            function4(ax4, xml)
        if 'save_csv' in option_list:
            function5(xml)

        handle_subplot(ax1, ax2, ax3, ax4)
        save_png_iv(xml)