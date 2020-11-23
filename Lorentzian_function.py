import matplotlib.pyplot as plt
from numpy import pi, sqrt, cos, arange, sin, around

wavelength_of_max_R = 555 * 10**(-9)
lorentzian_width = 1 * 10**(-9)
massive_of_wavelengths_of_max_R = [400 * 10**(-9), 550 * 10**(-9), 700 * 10**(-9)]
massive_of_lorentzian_widths = [0.5 * 10**(-9), 2 * 10**(-9), 5 * 10**(-9)]
massive_of_wavelengths = arange(380, 780, 1) * 10**(-9)

need_to_plot_f_vs_wavelength = False
need_to_plot_f_vs_wavelength_and_wavelengths_of_max_R = True
need_to_plot_f_vs_wavelength_and_lorentzian_width = True


def plotting(fig, massive_of_wavelengths, wavelength_of_max_R, lorentzian_width, info_for_label): #строим график R(длина волны, ?)
    f = 1 / pi * lorentzian_width / ((massive_of_wavelengths - wavelength_of_max_R)**2 + lorentzian_width**2)
    plt.plot(massive_of_wavelengths, f, label = info_for_label)

def settings_of_graph(fig): #настройки графика R(длина волны, ?)
    plt.legend(loc = 'best')
    plt.ylabel('f')
    plt.xlabel('Длина волны, нм')
    plt.grid(True)

if need_to_plot_f_vs_wavelength:
    plotting(fig, massive_of_wavelengths, massive_of_wavelengths_of_max_R, lorentzian_width, info_for_label = None)
    plt.title('Спектр отражения. Длина волны с максимумом коэф отражения: '+str(wavelength_of_max_R / 10**(-9))+' нм. Ширина Лоренциана: '+str(lorentzian_width))
    settings_of_graph(fig)

if need_to_plot_f_vs_wavelength_and_wavelengths_of_max_R: #строим график R(длина волны, толщина плёнки)
    fig = plt.figure()
    for i in range(len(massive_of_wavelengths_of_max_R)):
        plotting(fig, massive_of_wavelengths, massive_of_wavelengths_of_max_R[i], lorentzian_width, info_for_label = 'Максимум в точке '+str(massive_of_wavelengths_of_max_R[i] / 10**(-9))+' nm')
    plt.title('Спектр отражения. Ширина Лоренциана: '+str(lorentzian_width))
    settings_of_graph(fig)

if need_to_plot_f_vs_wavelength_and_lorentzian_width:
    fig = plt.figure()
    for i in range(len(massive_of_lorentzian_widths)):
        plotting(fig, massive_of_wavelengths, wavelength_of_max_R, massive_of_lorentzian_widths[i], info_for_label = 'Ширина Лоренциана '+str(massive_of_lorentzian_widths[i]))
    plt.title('Спектр отражения. Максимум в точке '+str(around((wavelength_of_max_R / 10**(-9)), 0))+' nm')
    settings_of_graph(fig)

plt.show()
