import matplotlib.pyplot as plt
from numpy import pi, sqrt, cos, arange, sin, around, meshgrid, linspace

wavelength = 555 #nanometers
film_thickness = 125#nanometers
incidence_angle = 0 #rad
n0 = 1
n1 = 2
n2 = 4

massive_of_wavelengths = arange(400, 50, 750) #nanometers
massive_of_film_thicknesses = arange(50, 550, 50) #nanometers
massive_of_incidence_angles = around(arange(0, pi/2, pi/20), 3) #rad
massive_of_incidence_angles = [0, 0.523, 0.7, 0.872] #для подгона графика из Хасса
massive_of_n0 = arange(1, 2.6, 0.2)
massive_of_n1 = arange(1, 2.6, 0.2)
massive_of_n2 = arange(1, 2.6, 0.2)

massive_of_wavelengths_for_x = arange(400, 800, 2) #nanometers
massive_of_incidence_angles_for_x = around(arange(0, pi/2, pi/400), 3) #rad

massive_of_wavelengths_for_2D = [450, 700] #максимум три штуки
massive_of_incidence_angles_for_2D = [0.1, 1] #максимум три штуки

need_to_plot_R_vs_wavelength = True
need_to_plot_R_vs_wavelength_and_film_thickness = False
need_to_plot_R_vs_wavelength_and_incidence_angle = False
need_to_plot_R_vs_wavelength_and_n0 = False
need_to_plot_R_vs_wavelength_and_n1 = False
need_to_plot_R_vs_wavelength_and_n2 = False

need_to_plot_R_vs_incidence_angle = False
need_to_plot_R_vs_incidence_angle_and_wavelength = False
need_to_plot_R_vs_incidence_angle_and_film_thickness = False

need_to_plot_2Dcolormap = False
need_to_plot_incidence_angle_vs_wavelength_with_2D = False
need_to_plot_wavelength_vs_incidence_angle_with_2D = False

def calculate_R(wavelength, film_thickness, incidence_angle, n0, n1, n2): #считаем значение коэффициента отражения
    cos_alpha = sqrt(1 - (n0 * sin(incidence_angle) / n1)**2 )
    cos_2fi = cos(4 * pi * n1 * film_thickness * cos_alpha / wavelength)
    r1 = (n0 - n1) / (n0 + n1)
    r2 = (n1 - n2) / (n1 + n2)
    R_numerator = r1**2 + r2**2 + 2 * r1 * r2 * cos_2fi
    R_denominator =  1 + (r1 * r2)**2 + 2 * r1 * r2 * cos_2fi
    R = R_numerator/R_denominator
    '''R = []
    for i in range(len(wavelength)):
        cos_refraction_angle = sqrt(1 - (n0 * sin(incidence_angle) / n1)**2 )
        two_fi = 4 * pi * n1 * film_thickness * cos(incidence_angle) / wavelength[i]
        two_fi1 = 4 * pi * n1 * film_thickness * cos_refraction_angle / wavelength[i]
        r1x = (n0 * cos(incidence_angle) - n1 * cos_refraction_angle) / (n0 * cos(incidence_angle) + n1 * cos_refraction_angle)
        r1y = 0#(n1 * cos(incidence_angle) - n0 * cos_refraction_angle) / (n1 * cos(incidence_angle) + n0 * cos_refraction_angle)
        r2x = (n1 * cos_refraction_angle - n2 * cos(incidence_angle)) / (n1 * cos_refraction_angle + n2 * cos(incidence_angle))
        r2y = 0#(n2 * cos_refraction_angle - n1 * cos(incidence_angle)) / (n2 * cos_refraction_angle + n1 * cos(incidence_angle))
        r1 = sqrt(r1x**2 + r1y**2)
        r2 = sqrt(r2x**2 + r2y**2)
        r_complex_numerator = complex(r1 + r2 * cos(two_fi), - r2 * sin(two_fi))
        r_complex_denominator = complex(1 + r1 * r2 * cos(two_fi1), - r2 * sin(two_fi1))
        r_complex = r_complex_numerator / r_complex_denominator
        R.append(abs(r_complex)**2)'''
    return R

def plotting_graph_where_x_is_wavelength(fig, film_thickness, incidence_angle, n0, n1, n2, info_for_label): #строим график R(длина волны, ?)
    global massive_of_wavelengths_for_x
    R = calculate_R(massive_of_wavelengths_for_x, film_thickness, incidence_angle, n0, n1, n2)
    plt.plot(massive_of_wavelengths_for_x, R, label = info_for_label)

def settings_of_graph_where_x_is_wavelength(fig): #настройки графика R(длина волны, ?)
    plt.legend(loc = 'best')
    plt.ylabel('R')
    plt.xlabel('Длина волны, нм')
    plt.grid(True)

def plotting_graph_where_x_is_incidence_angle(fig, film_thickness, wavelength, n0, n1, n2, info_for_label): #строим график R(угол падения, ?)
    global massive_of_incidence_angles_for_x
    R = calculate_R(wavelength, film_thickness, massive_of_incidence_angles_for_x, n0, n1, n2)
    plt.plot(massive_of_incidence_angles_for_x, R, label = info_for_label)
    
def settings_of_graph_where_x_is_incidence_angle(fig): #настройки графика R(угол падения, ?)
    plt.legend(loc = 'best')
    plt.ylabel('R')
    plt.xlabel('Угол падения, рад')
    plt.grid(True)

if need_to_plot_R_vs_wavelength: #строим график R(длина волны)
    fig = plt.figure()
    plotting_graph_where_x_is_wavelength(fig, film_thickness, incidence_angle, n0, n1, n2, info_for_label = None)
    plt.title('График R(длина волны). Толщина плёнки = ' +str(film_thickness)+' nm, угол падения = '+str(around(incidence_angle/3.14, 3))+'pi, n0 = '+str(n0)+', n1 = ' +str(n1)+', n2 = '+str(n2))
    settings_of_graph_where_x_is_wavelength(fig)

if need_to_plot_R_vs_wavelength_and_film_thickness: #строим график R(длина волны, толщина плёнки)
    fig = plt.figure()
    for i in range(len(massive_of_film_thicknesses)):
        plotting_graph_where_x_is_wavelength(fig, massive_of_film_thicknesses[i], incidence_angle, n0, n1, n2, info_for_label = 'Толщина плёнки = '+str(massive_of_film_thicknesses[i])+' nm')
    plt.title('График R(длина волны). Угол падения = '+str(around(incidence_angle/3.14, 3))+'pi, n0 = '+str(n0)+', n1 = ' +str(n1)+', n2 = '+str(n2))
    settings_of_graph_where_x_is_wavelength(fig)

if need_to_plot_R_vs_wavelength_and_incidence_angle: #строим график R(длина волны, угол падения)
    fig = plt.figure()
    for i in range(len(massive_of_incidence_angles)):
        plotting_graph_where_x_is_wavelength(fig, film_thickness, massive_of_incidence_angles[i], n0, n1, n2, info_for_label = 'Угол падения = '+str(round(massive_of_incidence_angles[i]/3.14,3))+'pi')
    plt.title('График R(длина волны). Толщина плёнки = '+str(film_thickness)+' nm, n0 = '+str(n0)+', n1 = ' +str(n1)+', n2 = '+str(n2))
    settings_of_graph_where_x_is_wavelength(fig)
    
if need_to_plot_R_vs_wavelength_and_n0: #строим график R(длина волны, коэф преломления внешней среды)
    fig = plt.figure()
    for i in range(len(massive_of_n0)):
        plotting_graph_where_x_is_wavelength(fig, film_thickness, incidence_angle, massive_of_n0[i], n1, n2, info_for_label = 'Коэф преломления внешней среды = '+str(around(massive_of_n0[i], 3)))
    plt.title('График R(длина волны). Толщина плёнки = '+str(film_thickness)+' nm, угол падения = '+str(around(incidence_angle/3.14, 3))+'pi, n1 = ' +str(n1)+', n2 = '+str(n2))
    settings_of_graph_where_x_is_wavelength(fig)

if need_to_plot_R_vs_wavelength_and_n1: #строим график R(длина волны, коэф преломления плёнки)
    fig = plt.figure()
    for i in range(len(massive_of_n1)):
        plotting_graph_where_x_is_wavelength(fig, film_thickness, incidence_angle, n0, massive_of_n1[i], n2, info_for_label = 'Коэф преломления плёнки = '+str(around(massive_of_n1[i], 3)))
    plt.title('График R(длина волны). Толщина плёнки = '+str(film_thickness)+' nm, угол падения = '+str(around(incidence_angle/3.14, 3))+'pi, n0 = ' +str(n0)+', n2 = '+str(n2))
    settings_of_graph_where_x_is_wavelength(fig)

if need_to_plot_R_vs_wavelength_and_n2: #строим график R(длина волны, коэф преломления подложки)
    fig = plt.figure()
    for i in range(len(massive_of_n2)):
        plotting_graph_where_x_is_wavelength(fig, film_thickness, incidence_angle, n0, n1, massive_of_n2[i], info_for_label = 'Коэф преломления подложки = '+str(around(massive_of_n2[i], 3)))
    plt.title('График R(длина волны). Толщина плёнки = '+str(film_thickness)+' nm, угол падения = '+str(around(incidence_angle/3.14, 3))+'pi, n0 = ' +str(n0)+', n1 = '+str(n1))
    settings_of_graph_where_x_is_wavelength(fig)
    
if need_to_plot_R_vs_incidence_angle: #строим график R(угол падения)
    fig = plt.figure()
    plotting_graph_where_x_is_incidence_angle(fig, film_thickness, wavelength, n0, n1, n2, info_for_label = None)
    plt.title('График R(угол падения). Длина волны = '+str(wavelength)+' nm, толщина плёнки = '+str(film_thickness)+' nm, n0 = '+str(n0)+', n1 = ' +str(n1)+', n2 = '+str(n2))
    settings_of_graph_where_x_is_incidence_angle(fig)
    
if need_to_plot_R_vs_incidence_angle_and_wavelength: #строим график R(угол падения, длина волны)
    fig = plt.figure()
    for i in range(len(massive_of_wavelengths)):
        plotting_graph_where_x_is_incidence_angle(fig, film_thickness, massive_of_wavelengths[i], n0, n1, n2, info_for_label = 'Длина волны = '+ str(massive_of_wavelengths[i])+' nm')
    plt.title('График R(угол падения). Толщина плёнки = '+str(film_thickness)+' nm, n0 = '+str(n0)+', n1 = ' +str(n1)+', n2 = '+str(n2))
    settings_of_graph_where_x_is_incidence_angle(fig)

if need_to_plot_R_vs_incidence_angle_and_film_thickness: #строим график R(угол падения, толщина плёнки)
    fig = plt.figure()
    for i in range(len(massive_of_film_thicknesses)):
        plotting_graph_where_x_is_incidence_angle(fig, massive_of_film_thicknesses[i], wavelength, n0, n1, n2, info_for_label = 'Толщина плёнки = '+ str(massive_of_film_thicknesses[i])+' nm')
    plt.title('График R(угол падения). Длина волны = '+str(wavelength)+' nm, n0 = '+str(n0)+', n1 = ' +str(n1)+', n2 = '+str(n2))
    settings_of_graph_where_x_is_incidence_angle(fig)

if need_to_plot_2Dcolormap: #строим 2d colormap R(длина волны, угол падения)
    fig = plt.figure()
    X, Y = meshgrid(massive_of_wavelengths_for_x, massive_of_incidence_angles_for_x)
    R = calculate_R(X, film_thickness, Y, n0, n1, n2)
    im = plt.pcolor(X, Y, R, cmap='jet')
    if need_to_plot_incidence_angle_vs_wavelength_with_2D:
        for i in range(len(massive_of_wavelengths_for_2D)):
            x = linspace(massive_of_wavelengths_for_2D[i],massive_of_wavelengths_for_2D[i],100)
            y = linspace(0,1.55,100)
            plt.plot(x, y,
                     linestyle = '--',
                     linewidth = 2,
                     color = 'Blue')
    if need_to_plot_wavelength_vs_incidence_angle_with_2D:
        for i in range(len(massive_of_incidence_angles_for_2D)):
            y = linspace(massive_of_incidence_angles_for_2D[i],massive_of_incidence_angles_for_2D[i],100)
            x = linspace(400,790,100)
            plt.plot(x, y,
                     linestyle = '--',
                     linewidth = 2,
                     color = 'Red')    
            plt.title('График R(угол падения). Длина волны = '+str(wavelength)+' nm, n0 = '+str(n0)+', n1 = ' +str(n1)+', n2 = '+str(n2))
    plt.colorbar(im)
    plt.title('2D colormap. R(длина волны, угол падения). Толщина плёнки = '+str(film_thickness)+' nm, n0 = '+str(n0)+', n1 = ' +str(n1)+', n2 = '+str(n2))
    plt.ylabel('Угол падения, рад')
    plt.xlabel('Длина волны, нм')

if need_to_plot_incidence_angle_vs_wavelength_with_2D:
    for i in range(len(massive_of_wavelengths_for_2D)):
        fig = plt.figure()
        plotting_graph_where_x_is_incidence_angle(fig, film_thickness, massive_of_wavelengths_for_2D[i], n0, n1, n2, info_for_label = None)
        plt.title('График R(угол падения). Длина волны = '+str(massive_of_wavelengths_for_2D[i])+' nm, толщина плёнки = '+str(film_thickness)+' nm, n0 = '+str(n0)+', n1 = ' +str(n1)+', n2 = '+str(n2))
        settings_of_graph_where_x_is_incidence_angle(fig)

if need_to_plot_wavelength_vs_incidence_angle_with_2D:
    for i in range(len(massive_of_incidence_angles_for_2D)):
        fig = plt.figure()
        plotting_graph_where_x_is_wavelength(fig, film_thickness, massive_of_incidence_angles_for_2D[i], n0, n1, n2, info_for_label = None)
        plt.title('График R(угол падения). Угол падения = '+str(around(massive_of_incidence_angles_for_2D[i]/pi, 3))+'pi, толщина плёнки = '+str(film_thickness)+' nm, n0 = '+str(n0)+', n1 = ' +str(n1)+', n2 = '+str(n2))
        settings_of_graph_where_x_is_wavelength(fig)
    
plt.show()
