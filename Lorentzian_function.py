import matplotlib.pyplot as plt
from numpy import pi, sqrt, cos, arange, sin, around, exp, array
from functions_for_plotting_CIE_diagram import CIE_diagram_plot

wavelength_of_max_R = 440 * 10**(-9)
lorentzian_width = 1 * 10**(-9)
massive_of_wavelengths_of_max_R = [400 * 10**(-9), 550 * 10**(-9), 700 * 10**(-9)]
massive_of_lorentzian_widths = [0.01 * 10**(-9), 5 * 10**(-9), 50 * 10**(-9)]
massive_of_wavelengths = arange(380, 780, 1) * 10**(-9)

need_to_plot_CIE_diagram = True
need_to_plot_f_vs_wavelength = False
need_to_plot_f_vs_wavelength_and_wavelengths_of_max_R = False
need_to_plot_f_vs_wavelength_and_lorentzian_width = False

def g(x, alpha, mu, sigma1, sigma2):
    res = array([(alpha * exp((xi - mu)**2 / (- 2 * sigma1**2)) if xi < mu else alpha * exp((xi - mu)**2 / (- 2 * sigma2**2))) for xi in x])
    return res

func_x = g(massive_of_wavelengths, 1.056, 5998*10**(-10), 379*10**(-10), 310*10**(-10)) + g(massive_of_wavelengths, 0.362, 4420*10**(-10), 160*10**(-10), 267*10**(-10)) + g(massive_of_wavelengths, -0.065, 5011*10**(-10), 204*10**(-10), 262*10**(-10))
func_y = g(massive_of_wavelengths, 0.821, 5688*10**(-10), 469*10**(-10), 405*10**(-10)) + g(massive_of_wavelengths, 0.286, 5309*10**(-10), 163*10**(-10), 311*10**(-10))
func_z = g(massive_of_wavelengths, 1.217, 4370*10**(-10), 118*10**(-10), 360*10**(-10)) + g(massive_of_wavelengths, 0.681, 4590*10**(-10), 260*10**(-10), 138*10**(-10))
         
func_of_incidence_spectrum = massive_of_wavelengths / massive_of_wavelengths
lorentzian_func = 1 / pi * lorentzian_width / ((massive_of_wavelengths - wavelength_of_max_R)**2 + lorentzian_width**2)

def integration(func, left_border = 380 * 10**(-9), right_border = 780 * 10**(-9)):
    res = 0.0
    for i in range(int((right_border - left_border) * 10**(9) / 2)):
        res = res + func[2 * i]* 2 * 10**(-9)
    return res

def plotting(fig, massive_of_wavelengths, wavelength_of_max_R, lorentzian_width, info_for_label): #строим график R(длина волны, ?)
    f = 1 / pi * lorentzian_width / ((massive_of_wavelengths - wavelength_of_max_R)**2 + lorentzian_width**2)
    f = f / max(f)
    plt.plot(massive_of_wavelengths, f, label = info_for_label)

def settings_of_graph(fig): #настройки графика R(длина волны, ?)
    plt.legend(loc = 'best')
    plt.ylabel('f')
    plt.xlabel('Длина волны, нм')
    plt.grid(True)

if need_to_plot_f_vs_wavelength:
    fig = plt.figure()
    plotting(fig, massive_of_wavelengths, wavelength_of_max_R, lorentzian_width, info_for_label = None)
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

if need_to_plot_CIE_diagram:
    massive_of_dots = []
    massive_of_widths = ['0.01 nm', '5 nm', '50 nm']
    for i in range(len(massive_of_lorentzian_widths)):
        lorentzian_func = 1 / pi * massive_of_lorentzian_widths[i] / ((massive_of_wavelengths - wavelength_of_max_R)**2 + massive_of_lorentzian_widths[i]**2) +  1 / pi * massive_of_lorentzian_widths[i] / ((massive_of_wavelengths - 620 * 10**(-9))**2 + massive_of_lorentzian_widths[i]**2)
        x = integration(func_x*func_of_incidence_spectrum*lorentzian_func)
        y = integration(func_y*func_of_incidence_spectrum*lorentzian_func)
        z = integration(func_z*func_of_incidence_spectrum*lorentzian_func)
        X = x / (x + y + z)
        Y = y / (x + y + z)
        Z = z / (x + y + z)
        print(X, Y, Z)
        massive_of_dots.append([X, Y, Z])
    CIE_diagram_plot(massive_of_dots, massive_of_widths, 'CIE diagram. Центры Лоренца - 440 и 620 нм. Падающий спектр - const')
    plt.show()
