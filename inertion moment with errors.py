import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10, 10))
plt.minorticks_on()


h_1 = [0, 0.4, 0.75, 1.5, 1.75, 1.2, 2.3, 4.0, 3.0, 3.7]
h_2 = [i ** 2 for i in h_1]

i_1 = [9.775, 9.858, 10.014, 10.175, 10.419, 10.121, 10.488, 12.069, 11.15, 11.7]


coef_1 = np.polyfit(h_2,i_1,1) 
poly1d_fn = np.poly1d(coef_1) 
 
plt.plot(h_2, poly1d_fn(h_2))


plt.xlim(-0.1, 17) 
plt.ylim(8, 13) 

plt.grid(which='minor')
y_error=[0.12, 0.13, 0.12, 0.1, 0.12, 0.14, 0.12, 0.1, 0.1, 0.1]
x_error=[0.15, 0.15, 0.16, 0.15, 0.18, 0.17, 0.15, 0.2, 0.2, 0.2]


plt.errorbar(h_2, i_1, xerr= x_error, yerr = y_error , fmt='none', ecolor = 'blue', color='yellow')

plt.plot(h_2, i_1, 'bo')

plt.ylabel(r'$I,  \ kg*m^2 \ 10^3$')
plt.xlabel(r'$h^2,  \ см$')
plt.title(r'$y=0.1369*10^3x+9.87263*10^3, \ r=0.994$') 
plt.grid(True)


plt.show()

