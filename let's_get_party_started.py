#гениальный код!!!
import matplotlib.pyplot as plt
from numpy import pi, sqrt, cos, arange, sin, around, meshgrid

wavelength = 555 #nanometers
film_thickness = 90.58#nanometers
incidence_angle = around(pi/10, 3) #rad
n0 = 1
n1 = 1.38
n2 = 1.51

massive_of_wavelengths = arange(400, 50, 750) #nanometers
massive_of_film_thicknesses = arange(50, 550, 50) #nanometers
massive_of_incidence_angles = around(arange(0, pi/2, pi/20), 3) #rad
massive_of_incidence_angles = [0, 0.523, 0.7, 0.872, 1.05] #для подгона графика из Хасса
massive_of_n0 = arange(1, 2.6, 0.2)
massive_of_n1 = arange(1, 2.6, 0.2)
massive_of_n2 = arange(1, 2.6, 0.2)

massive_of_wavelengths_for_x = arange(400, 800, 2) #nanometers
massive_of_incidence_angles_for_x = around(arange(0, pi/2, pi/400), 3) #rad

need_to_plot_R_vs_wavelength = False
need_to_plot_R_vs_wavelength_and_film_thickness = False
need_to_plot_R_vs_wavelength_and_incidence_angle = False
need_to_plot_R_vs_wavelength_and_n0 = False
need_to_plot_R_vs_wavelength_and_n1 = False
need_to_plot_R_vs_wavelength_and_n2 = False

need_to_plot_R_vs_incidence_angle = False
need_to_plot_R_vs_incidence_angle_and_wavelength = False
need_to_plot_R_vs_incidence_angle_and_film_thickness = False

need_to_plot_2Dcolormap = True

def calculate_R(wavelength, film_thickness, incidence_angle, n0, n1, n2): #считаем значение коэффициента отражения
    cos_alpha = sqrt(1 - (n0 * sin(incidence_angle) / n1)**2 )
    cos_2fi = cos(4 * pi * n1 * film_thickness * cos_alpha / wavelength)
    r1 = (n0 - n1) / (n0 + n1)
    r2 = (n1 - n2) / (n1 + n2)
    R_numerator = r1**2 + r2**2 + 2 * r1 * r2 * cos_2fi
    R_denominator =  1 + (r1 * r2)**2 + 2 * r1 * r2 * cos_2fi
    R = R_numerator/R_denominator
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
    
if need_to_plot_R_vs_incidence_angle:
    fig = plt.figure()
    plotting_graph_where_x_is_incidence_angle(fig, film_thickness, wavelength, n0, n1, n2, info_for_label = None)
    plt.title('График R(угол падения). Длина волны = '+str(wavelength)+' nm, толщина плёнки = '+str(film_thickness)+' nm, n0 = '+str(n0)+', n1 = ' +str(n1)+', n2 = '+str(n2))
    settings_of_graph_where_x_is_incidence_angle(fig)
    
if need_to_plot_R_vs_incidence_angle_and_wavelength:
    fig = plt.figure()
    for i in range(len(massive_of_wavelengths)):
        plotting_graph_where_x_is_incidence_angle(fig, film_thickness, massive_of_wavelengths[i], n0, n1, n2, info_for_label = 'Длина волны = '+ str(massive_of_wavelengths[i])+' nm')
    plt.title('График R(угол падения). Толщина плёнки = '+str(film_thickness)+' nm, n0 = '+str(n0)+', n1 = ' +str(n1)+', n2 = '+str(n2))
    settings_of_graph_where_x_is_incidence_angle(fig)

if need_to_plot_R_vs_incidence_angle_and_film_thickness:
    fig = plt.figure()
    for i in range(len(massive_of_film_thicknesses)):
        plotting_graph_where_x_is_incidence_angle(fig, massive_of_film_thicknesses[i], wavelength, n0, n1, n2, info_for_label = 'Толщина плёнки = '+ str(massive_of_film_thicknesses[i])+' nm')
    plt.title('График R(угол падения). Длина волны = '+str(wavelength)+' nm, n0 = '+str(n0)+', n1 = ' +str(n1)+', n2 = '+str(n2))
    settings_of_graph_where_x_is_incidence_angle(fig)

if need_to_plot_2Dcolormap:
    X, Y = meshgrid(massive_of_wavelengths_for_x, massive_of_incidence_angles_for_x)
    R = calculate_R(X, film_thickness, Y, n0, n1, n2)
    im = plt.pcolor(X, Y, R, cmap=plt.cm.RdBu)
    plt.colorbar(im)
    plt.title('2D colormap. R(длина волны, угол падения). Толщина плёнки = '+str(film_thickness)+' nm, n0 = '+str(n0)+', n1 = ' +str(n1)+', n2 = '+str(n2))
    plt.ylabel('Угол падения, рад')
    plt.xlabel('Длина волны, нм')
    
plt.show()
