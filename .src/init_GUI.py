import tkinter as tk
import customtkinter


def init_GUI(self):
    method_var1 = customtkinter.IntVar()
    method_var2 = customtkinter.IntVar()

    customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

    # 창 생성
    self.title("Wafer Analysis")
    self.geometry(f"{1050}x{700}")

    # configure grid layout (4x4)
    self.grid_columnconfigure(1, weight=1)
    self.grid_columnconfigure((2, 3), weight=1)
    self.grid_rowconfigure((0, 1, 2), weight=1)

    # 왼쪽 위젯 프레임
    self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
    self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
    self.sidebar_frame.grid_rowconfigure(4, weight=1)
    # 왼쪽 젤 위에 글씨
    self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Wafer Analysis",
                                             font=customtkinter.CTkFont(size=20, weight="bold"))
    self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
    # 왼쪽에 위젯 버튼
    self.checkbox_1 = customtkinter.CTkCheckBox(master=self.sidebar_frame, text="save png", variable=method_var1)
    self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="nw")
    self.checkbox_2 = customtkinter.CTkCheckBox(master=self.sidebar_frame, text="save csv", variable=method_var2)
    self.checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="nw")
    # 왼쪽 아래 라이트, 다크 모드
    self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
    self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
    self.appearance_mode_optionmenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                  values=["Light", "Dark", "System"],
                                                                  command=self.change_appearance_mode_event)
    self.appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=(10, 10))
    self.appearance_mode_optionmenu.set("Light")
    # 왼쪽 아래 화면 배율
    self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
    self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
    self.scaling_optionmenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                          values=["80%", "90%", "100%", "110%", "120%"],
                                                          command=self.change_scaling_event)
    self.scaling_optionmenu.grid(row=8, column=0, padx=20, pady=(10, 20))
    self.scaling_optionmenu.set("100%")

    # 왼 쪽에서 두번째 줄 tab 창(lot, wafer, location, date)
    self.tabview = customtkinter.CTkTabview(self)
    self.tabview.grid(row=0, rowspan=3, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
    self.tabview.add("Lot ID")
    self.tabview.add("Wafer ID")
    self.tabview.add("Location")
    self.tabview.add("Date")
    self.tabview.tab("Lot ID").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
    self.tabview.tab("Wafer ID").grid_columnconfigure(0, weight=1)
    self.tabview.tab("Location").grid_columnconfigure(0, weight=1)
    self.tabview.tab("Date").grid_columnconfigure(0, weight=1)

    self.num_files_label = customtkinter.CTkLabel(self, text="Number of Files: 0")
    self.num_files_label.grid(row=3, column=1, sticky="n", pady=10)

    # set scale
    self.sidebar_button_1 = customtkinter.CTkButton(self, command=self.save_choosed_data, text="set scale")
    self.sidebar_button_1.grid(row=3, column=1,sticky="ne", pady=10)

    # progress bar
    self.progress_value = customtkinter.DoubleVar()
    self.progress_ratio_label = customtkinter.CTkLabel(self, text="Progress ratio:  0%")
    self.progress_ratio_label.grid(row=3, column=1, padx=30, pady=0, sticky="ws")
    self.progress_bar = customtkinter.CTkProgressBar(self, determinate_speed=0, mode="determinate",
                                                     variable=self.progress_value)
    self.progress_bar.grid(row=4, column=1, columnspan=2, padx=20, pady=(0, 20), sticky="nsew")

    self.choose_dict = {}
    self.lot_list = []
    self.wafer_list = []
    self.coordinate_list = []
    self.date_list = []

    # tabview에 글씨 넣기
    self.select_listbox1 = tk.Listbox(self.tabview.tab("Lot ID"), width=30, height=15, selectmode='multiple',
                                      exportselection=0)
    self.select_listbox1.grid(row=1, column=0, padx=5, pady=5)
    self.select_listbox1.configure(background='#F9F9FA')

    self.select_listbox2 = tk.Listbox(self.tabview.tab("Wafer ID"), width=30, height=15, selectmode='multiple',
                                      exportselection=0)
    self.select_listbox2.grid(row=1, column=0, padx=5, pady=5)
    self.select_listbox2.configure(background='#F9F9FA')

    self.select_listbox3 = tk.Listbox(self.tabview.tab("Location"), width=30, height=15, selectmode='multiple',
                                      exportselection=0)
    self.select_listbox3.grid(row=1, column=0, padx=5, pady=5)
    self.select_listbox3.configure(background='#F9F9FA')

    self.select_listbox4 = tk.Listbox(self.tabview.tab("Date"), width=30, height=15, selectmode='multiple',
                                      exportselection=0)
    self.select_listbox4.grid(row=1, column=0, padx=5, pady=5)
    self.select_listbox4.configure(background='#F9F9FA')

    # selected xml files 표기용 박스
    self.tabview_2 = customtkinter.CTkTabview(self,state='disabled', bg_color="transparent")
    self.tabview_2.grid(row=0, rowspan=3, column=2, columnspan=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
    self.tabview_2.add("Selected XML files")
    self.textbox = customtkinter.CTkTextbox(self, width=110, height=100, state='disabled')
    self.textbox.grid(row=0, rowspan=3, column=2, columnspan=2, padx=(30, 30), pady=(70, 30), sticky="nsew")

    # 오른쪽 아래 analyze button
    self.analyze_button_1 = customtkinter.CTkButton(master=self, fg_color="#3B8ED0", border_width=0,
                                                    text_color="#DCE4EE", text="analyze",
                                                    command=lambda: self.analyze_data([
                                                        'png' if method_var1.get() else None,
                                                        'csv' if method_var2.get() else None]))
    self.analyze_button_1.grid(row=3, column=3, padx=(20, 20), pady=(10, 20), sticky="nsew")

    # 오른쪽 아래 exit button
    self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2,
                                                 text_color=("gray10", "#DCE4EE"), text="exit",
                                                 command=self.exit_app)
    self.main_button_1.grid(row=4, column=3, padx=(20, 20), pady=(0, 20), sticky="nsew")

    self.choose_analysis_scale()
