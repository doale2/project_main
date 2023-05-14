import numpy as np
from lmfit import Model


def fit_IV(voltage, I_s, q, nkT):
    return I_s * (np.exp(q * voltage / nkT) - 1)


def iv_fitting(iv_data):
    # Threshold voltage 기준으로 구간 설정
    x_bef_Vth, x_aft_Vth = iv_data['voltage'][:10], iv_data['voltage'][9:]
    y_bef_Vth, y_aft_Vth = iv_data['current'][:10], iv_data['current'][9:]
    # Threshold voltage 이전
    fp = np.polyfit(x_bef_Vth, y_bef_Vth, 8)  # Data point가 10개 이므로 8차까지 해야 근사에 의미가 있음
    f = np.poly1d(fp)  # Equation으로 만듬
    # Threshold voltage 이후
    I_s = iv_data['current'][0]
    model = Model(fit_IV)
    params = model.make_params(I_s=I_s, q=1, nkT=1)  # 변수들을 값을 고정하거나 초기화 함
    # Fit the model to the data
    result = model.fit(y_aft_Vth, params, voltage=x_aft_Vth)  # 최고의 fitting 결과를 result에 가져옴
    # 두 개의 fitting 결과를 하나의 리스트로 합침
    y_fit = list(f(x_bef_Vth))
    y_fit.extend(result.best_fit[1:])
    return y_fit
