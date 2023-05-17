import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10, 10))
plt.minorticks_on()


x = [0.406, 0.324, 0.261, 0.213, 0.168]
y = [0.20, 0.153, 0.136, 0.11, 0.0873]



plt.xlim(0.15, 0.45) 
plt.ylim(0.07, 0.25) 

plt.grid(which='major')


coef = np.polyfit(x,y,1) 
poly1d_fn = np.poly1d(coef) 
 
plt.plot(x, poly1d_fn(x), 'b--')

x_error= [0.006, 0.005, 0.004, 0.002, 0.002]
y_error = [0.00079, 0.00062, 0.00049, 0.00038, 0.0003]
plt.plot(x, y, 'ro')
plt.errorbar(x, y, xerr= x_error, yerr = y_error , fmt='none', ecolor = 'blue', color='yellow')

plt.ylabel(r'$Ω,  \ 1/с$')
plt.xlabel(r'$М,  \ H*м$')
plt.title(r'$ Ω(М) \ f(x)=0.458x+0.0117, \ r=0.99454$') 
plt.grid(True)


plt.show()
