#гениальный код!!!
import matplotlib.pyplot as plt
from numpy import pi, sqrt, cos, arange, sin, around

wavelength = 555 #nanometers
film_thickness = 150 #nanometers
incidence_angle = around(pi/10, 3) #rad
n0 = 1
n1 = 1.38
n2 = 1.57
massive_of_wavelengths = arange(400, 800, 5) #nanometers
massive_of_film_thicknesses = arange(50, 550, 50) #nanometers
massive_of_incidence_angles = around(arange(0, pi/2, pi/200), 3) #rad
massive_of_n0 = arange(1, 2.6, 0.2)
massive_of_n1 = arange(1, 2.6, 0.2)
massive_of_n2 = arange(1, 2.6, 0.2)

global fig
fig = plt.figure()

def plotting_graph_where_x_is_incidence_angle(film_thickness, wavelength, n0, n1, n2, info_for_label): #строим график R(угол падения)
    global fig, massive_of_incidence_angles
    cosinus_2delta = cos(4*pi*n1*film_thickness*cos(massive_of_incidence_angles)/wavelength)
    R_numerator = (n0**2+n1**2)*(n1**2+n2**2)-4*n0*n1**2*n2+(n0**2-n1**2)*(n1**2-n2**2)*cosinus_2delta
    R_denominator = (n0**2+n1**2)*(n1**2+n2**2)+4*n0*n1**2*n2+(n0**2-n1**2)*(n1**2-n2**2)*cosinus_2delta
    plt.plot(massive_of_incidence_angles, R_numerator/R_denominator, label = info_for_label)

def plotting_graph_where_x_is_wavelength(film_thickness, incidence_angle, n0, n1, n2, info_for_label): #строим график R(длина волны)
    global fig, massive_of_wavelengths
    cosinus_2delta = cos(4*pi*n1*film_thickness*cos(incidence_angle)/massive_of_wavelengths)
    R_numerator = (n0**2+n1**2)*(n1**2+n2**2)-4*n0*n1**2*n2+(n0**2-n1**2)*(n1**2-n2**2)*cosinus_2delta
    R_denominator = (n0**2+n1**2)*(n1**2+n2**2)+4*n0*n1**2*n2+(n0**2-n1**2)*(n1**2-n2**2)*cosinus_2delta
    plt.plot(massive_of_wavelengths, R_numerator/R_denominator, label = info_for_label)

print('''Какой график будем строить? Нажми:
         0, если устал и хочешь спать;
         1, если R(угол падения);
         2, если R(длина волны)''')
choice_of_graph = int(input())

if choice_of_graph == 1:
    print('''Будут ли какие-нить дополнительные параметры на графике (несколько кривых)? Нажми:
             0, если ничего не нужно;
             1, если нужен доп параметр "длина волны";
             2, если нужен доп параметр "толщина плёнки"''')
    choice_of_parameter = int(input())
    
    if choice_of_parameter == 0: #Рисуем график R(угол падения) без доп параметров
        print('По умолчанию толщина плёнки равна '+str(film_thickness)+' nm, длина волны равна '+str(wavelength)+' nm, n0 = '+str(n0)+', n1 = ' +str(n1)+', n2 = '+str(n2))
        print('Если хотите что-то изменить, нажмите 1. Если всё ок, нажмите 0')
        want_to_change = int(input())
        if want_to_change == 1:
            print('Введите через запятую без пробелов значения системы в порядке: толщина плёнки (нм), длина волны (нм), n0, n1, n2')
            values = str(input())
            values = values.split(',')
            film_thickness = int(values[0])
            wavelength = int(values[1])
            n0 = float(values[2])
            n1 = float(values[3])
            n2 = float(values[4])
        plotting_graph_where_x_is_incidence_angle(film_thickness, wavelength, n0, n1, n2, info_for_label = None)
        plt.title('График R(угол падения). Толщина плёнки = '+str(film_thickness)+' nm, Длина волны = '+str(wavelength)+' nm, n0 = '+str(n0)+', n1 = ' +str(n1)+', n2 = '+str(n2))
        
    elif choice_of_parameter == 1: #Рисуем график R(угол падения) с доп параметром "длина волны"
        print('По умолчанию массив длин волн такой: ' + str(massive_of_wavelengths))
        print('Если хотите его изменить, нажмите 1. Если всё ок, нажмите 0')
        want_to_change = int(input())
        if want_to_change == 1:
            print('Введите 3 числа через запятую без пробелов, с помощью которых мы зададим массив: минимальное значение, максимальное значение и шаг.')
            values_for_massive = str(input())
            values_for_massive = values_for_massive.split(',')
            massive_of_wavelengths = arange(float(values_for_massive[0]), float(values_for_massive[1]), float(values_for_massive[2]))
        print('По умолчанию толщина плёнки равна '+str(film_thickness)+' nm, n0 = '+str(n0)+' , n1 = ' +str(n1)+' , n2 = '+str(n2))
        print('Если хотите что-то изменить, нажмите 1. Если всё ок, нажмите 0')
        want_to_change = int(input())
        if want_to_change == 1:
            print('Введите через запятую без пробелов значения системы в порядке: толщина плёнки (нм), n0, n1, n2')
            values = str(input())
            values = values.split(',')
            film_thickness = float(values[0])
            n0 = float(values[1])
            n1 = float(values[2])
            n2 = float(values[3])
        for i in range(len(massive_of_wavelengths)):
            plotting_graph_where_x_is_incidence_angle(film_thickness, massive_of_wavelengths[i], n0, n1, n2, info_for_label = 'Длина волны = '+ str(massive_of_wavelengths[i])+' nm')
        plt.title('График R(угол падения). Толщина плёнки = '+str(film_thickness)+' nm, n0 = '+str(n0)+', n1 = ' +str(n1)+', n2 = '+str(n2))
        
    elif choice_of_parameter == 2: #Рисуем график R(угол падения) с доп параметром "толщина плёнки"
        print('По умолчанию массив толщин плёнки такой: ' + str(massive_of_film_thicknesses))        
        print('Если хотите его изменить, нажмите 1. Если всё ок, нажмите 0')
        want_to_change = int(input())
        if want_to_change == 1:
            print('Введите 3 числа через запятую без пробелов, с помощью которых мы зададим массив: минимальное значение, максимальное значение и шаг.')
            values_for_massive = str(input())
            values_for_massive = values_for_massive.split(',')
            massive_of_film_thicknesses = arange(float(values_for_massive[0]), float(values_for_massive[1]), float(values_for_massive[2]))
        print('По умолчанию длина волны равна '+str(wavelength)+' nm, n0 = '+str(n0)+', n1 = ' +str(n1)+', n2 = '+str(n2))
        print('Если хотите что-то изменить, нажмите 1. Если всё ок, нажмите 0')
        want_to_change = int(input())
        if want_to_change == 1:
            print('Введите через запятую без пробелов значения системы в порядке: длина волны (нм), n0, n1, n2')
            values = str(input())
            values = values.split(',')
            wavelength = int(values[0])
            n0 = float(values[1])
            n1 = float(values[2])
            n2 = float(values[3])
        for i in range(len(massive_of_film_thicknesses)):
            plotting_graph_where_x_is_incidence_angle(massive_of_film_thicknesses[i], wavelength, n0, n1, n2, info_for_label = 'Толщина плёнки = '+ str(massive_of_film_thicknesses[i])+' nm')
        plt.title('График R(угол падения). Длина волны = '+str(wavelength)+' nm, n0 = '+str(n0)+', n1 = ' +str(n1)+', n2 = '+str(n2))
    plt.legend(loc = 'best')
    plt.ylabel('R')
    plt.xlabel('Угол падения, рад')
    plt.grid(True)
    plt.show()

        
elif choice_of_graph == 2: 
    print('''Будут ли какие-нить дополнительные параметры на графике (несколько кривых)? Нажми:
             0, если ничего не нужно;
             1, если нужен доп параметр "толщина плёнки";
             2, если нужен доп параметр "угол падения";
             3, если нужен доп параметр "коэф преломления внешней среды";
             4, если нужен доп параметр "коэф преломления плёнки";
             5, если нужен доп параметр "коэф преломления подложки"''')
    choice_of_parameter = int(input())

    if choice_of_parameter == 0: #Рисуем график R(длина волны) без доп параметров
        print('По умолчанию толщина плёнки равна '+str(film_thickness)+' nm, угол падения равен '+str(around(incidence_angle/3.14, 3))+'pi, n0 = '+str(n0)+', n1 = ' +str(n1)+', n2 = '+str(n2))
        print('Если хотите что-то изменить, нажмите 1. Если всё ок, нажмите 0')
        want_to_change = int(input())
        if want_to_change == 1:
            print('Введите через запятую без пробелов значения системы в порядке: толщина плёнки (нм), угол падения (рад), n0, n1, n2')
            values = str(input())
            values = values.split(',')
            film_thickness = int(values[0])
            incidence_angle = int(values[1])
            n0 = float(values[2])
            n1 = float(values[3])
            n2 = float(values[4])
        plotting_graph_where_x_is_wavelength(film_thickness, incidence_angle, n0, n1, n2, info_for_label = None)
        plt.title('График R(длина волны). Толщина плёнки = '+str(film_thickness)+' nm, угол падения '+str(around(incidence_angle/3.14, 3))+'pi, n0 = '+str(n0)+', n1 = ' +str(n1)+', n2 = '+str(n2))

    elif choice_of_parameter == 1: #Рисуем график R(длина волны) с доп параметром "толщина плёнки"
        print('По умолчанию массив толщин плёнки такой: ' + str(massive_of_film_thicknesses))        
        print('Если хотите его изменить, нажмите 1. Если всё ок, нажмите 0')
        want_to_change = int(input())
        if want_to_change == 1:
            print('Введите 3 числа через запятую без пробелов, с помощью которых мы зададим массив: минимальное значение, максимальное значение и шаг.')
            values_for_massive = str(input())
            values_for_massive = values_for_massive.split(',')
            massive_of_film_thicknesses = arange(float(values_for_massive[0]), float(values_for_massive[1]), float(values_for_massive[2]))
        print('По умолчанию угол падения равен '+str(around(incidence_angle/3.14, 3))+'pi, n0 = '+str(n0)+', n1 = ' +str(n1)+', n2 = '+str(n2))
        print('Если хотите что-то изменить, нажмите 1. Если всё ок, нажмите 0')
        want_to_change = int(input())
        if want_to_change == 1:
            print('Введите через запятую без пробелов значения системы в порядке: угол падения (рад), n0, n1, n2')
            values = str(input())
            values = values.split(',')
            incidence_angle = int(values[0])
            n0 = float(values[1])
            n1 = float(values[2])
            n2 = float(values[3])
        for i in range(len(massive_of_film_thicknesses)):
            plotting_graph_where_x_is_wavelength(massive_of_film_thicknesses[i], incidence_angle, n0, n1, n2, info_for_label = 'Толщина плёнки = '+str(massive_of_film_thicknesses[i])+' nm')
        plt.title('График R(длина волны). Угол падения = '+str(around(incidence_angle/3.14, 3))+'pi, n0 = '+str(n0)+', n1 = ' +str(n1)+', n2 = '+str(n2))

    elif choice_of_parameter == 2: #Рисуем график R(длина волны) с доп параметром "угол падения"
        print('По умолчанию массив углов падения такой: ' + str(around(massive_of_incidence_angles, 3)))        
        print('Если хотите его изменить, нажмите 1. Если всё ок, нажмите 0')
        want_to_change = int(input())
        if want_to_change == 1:
            print('Введите 3 числа через запятую без пробелов, с помощью которых мы зададим массив: минимальное значение, максимальное значение и шаг.')
            values_for_massive = str(input())
            values_for_massive = values_for_massive.split(',')
            massive_of_incidence_angles = arange(float(values_for_massive[0]), float(values_for_massive[1]), float(values_for_massive[2]))
        print('Толщина плёнки равна '+str(film_thickness)+' nm, n0 = '+str(n0)+', n1 = ' +str(n1)+', n2 = '+str(n2))
        print('Если хотите что-то изменить, нажмите 1. Если всё ок, нажмите 0')
        want_to_change = int(input())
        if want_to_change == 1:
            print('Введите через запятую без пробелов значения системы в порядке: толщина плёнки (нм), n0, n1, n2')
            values = str(input())
            values = values.split(',')
            film_thickness = int(values[0])
            n0 = float(values[1])
            n1 = float(values[2])
            n2 = float(values[3])
        for i in range(len(massive_of_incidence_angles)):
            plotting_graph_where_x_is_wavelength(film_thickness, massive_of_incidence_angles[i], n0, n1, n2, info_for_label = 'Угол падения = '+str(round(massive_of_incidence_angles[i]/3.14,3))+'pi')
        plt.title('График R(длина волны). Толщина плёнки = '+str(film_thickness)+' nm, n0 = '+str(n0)+', n1 = ' +str(n1)+', n2 = '+str(n2))

    elif choice_of_parameter == 3: #Рисуем график R(длина волны) с доп параметром "коэф преломления внешней среды"
        print('По умолчанию массив коэфов преломления внешней среды такой: ' + str(massive_of_n0))        
        print('Если хотите его изменить, нажмите 1. Если всё ок, нажмите 0')
        want_to_change = int(input())
        if want_to_change == 1:
            print('Введите 3 числа через запятую без пробелов, с помощью которых мы зададим массив: минимальное значение, максимальное значение и шаг.')
            values_for_massive = str(input())
            values_for_massive = values_for_massive.split(',')
            massive_of_n0 = arange(float(values_for_massive[0]), float(values_for_massive[1]), float(values_for_massive[2]))
        print('Толщина плёнки равна '+str(film_thickness)+' nm, угол падения'+str(around(incidence_angle/3.14, 3))+'pi, n1 = ' +str(n1)+', n2 = '+str(n2))
        print('Если хотите что-то изменить, нажмите 1. Если всё ок, нажмите 0')
        want_to_change = int(input())
        if want_to_change == 1:
            print('Введите через запятую без пробелов значения системы в порядке: толщина плёнки (нм), угол падения (рад), n1, n2')
            values = str(input())
            values = values.split(',')
            film_thickness = int(values[0])
            incidence_angle = float(values[1])
            n1 = float(values[2])
            n2 = float(values[3])
        for i in range(len(massive_of_n0)):
            plotting_graph_where_x_is_wavelength(film_thickness, incidence_angle, massive_of_n0[i], n1, n2, info_for_label = 'Коэф преломления внешней среды = '+str(around(massive_of_n0[i], 3)))
        plt.title('График R(длина волны). Толщина плёнки = '+str(film_thickness)+' nm, угол падения = '+str(around(incidence_angle/3.14, 3))+'pi, n1 = ' +str(n1)+', n2 = '+str(n2))

    elif choice_of_parameter == 4: #Рисуем график R(длина волны) с доп параметром "коэф преломления плёнки"
        print('По умолчанию массив коэфов преломления плёнки такой: ' + str(massive_of_n1))        
        print('Если хотите его изменить, нажмите 1. Если всё ок, нажмите 0')
        want_to_change = int(input())
        if want_to_change == 1:
            print('Введите 3 числа через запятую без пробелов, с помощью которых мы зададим массив: минимальное значение, максимальное значение и шаг.')
            values_for_massive = str(input())
            values_for_massive = values_for_massive.split(',')
            massive_of_n1 = arange(float(values_for_massive[0]), float(values_for_massive[1]), float(values_for_massive[2]))
        print('Толщина плёнки равна '+str(film_thickness)+' nm, угол падения'+str(around(incidence_angle/3.14, 3))+'pi, n0 = ' +str(n1)+', n2 = '+str(n2))
        print('Если хотите что-то изменить, нажмите 1. Если всё ок, нажмите 0')
        want_to_change = int(input())
        if want_to_change == 1:
            print('Введите через запятую без пробелов значения системы в порядке: толщина плёнки (нм), угол падения (рад), n0, n2')
            values = str(input())
            values = values.split(',')
            film_thickness = int(values[0])
            incidence_angle = float(values[1])
            n0 = float(values[2])
            n2 = float(values[3])
        for i in range(len(massive_of_n1)):
            plotting_graph_where_x_is_wavelength(film_thickness, incidence_angle, n0, massive_of_n1[i], n2, info_for_label = 'Коэф преломления плёнки = '+str(around(massive_of_n1[i], 3)))
        plt.title('График R(длина волны). Толщина плёнки = '+str(film_thickness)+' nm, угол падения = '+str(around(incidence_angle/3.14, 3))+'pi, n0 = ' +str(n0)+', n2 = '+str(n2))

    elif choice_of_parameter == 5: #Рисуем график R(длина волны) с доп параметром "коэф преломления подложки"
        print('По умолчанию массив коэфов преломления подложки такой: ' + str(massive_of_n2))        
        print('Если хотите его изменить, нажмите 1. Если всё ок, нажмите 0')
        want_to_change = int(input())
        if want_to_change == 1:
            print('Введите 3 числа через запятую без пробелов, с помощью которых мы зададим массив: минимальное значение, максимальное значение и шаг.')
            values_for_massive = str(input())
            values_for_massive = values_for_massive.split(',')
            massive_of_n2 = arange(float(values_for_massive[0]), float(values_for_massive[1]), float(values_for_massive[2]))
        print('Толщина плёнки равна '+str(film_thickness)+' nm, угол падения'+str(around(incidence_angle/3.14, 3))+'pi, n0 = ' +str(n1)+', n1 = '+str(n2))
        print('Если хотите что-то изменить, нажмите 1. Если всё ок, нажмите 0')
        want_to_change = int(input())
        if want_to_change == 1:
            print('Введите через запятую без пробелов значения системы в порядке: толщина плёнки (нм), угол падения (рад), n0, n1')
            values = str(input())
            values = values.split(',')
            film_thickness = int(values[0])
            incidence_angle = float(values[1])
            n0 = float(values[2])
            n1 = float(values[3])
        for i in range(len(massive_of_n2)):
            plotting_graph_where_x_is_wavelength(film_thickness, incidence_angle, n0, n1, massive_of_n2[i], info_for_label = 'Коэф преломления подложки = '+str(around(massive_of_n2[i], 3)))
        plt.title('График R(длина волны). Толщина плёнки = '+str(film_thickness)+' nm, угол падения = '+str(around(incidence_angle/3.14, 3))+'pi, n0 = ' +str(n0)+', n1 = '+str(n1))
        
    plt.legend(loc = 'best')
    plt.ylabel('R')
    plt.xlabel('Длина волны, нм')
    plt.grid(True)
    plt.show()

else:
    print('Спокойной ночи!')

    
        
    
