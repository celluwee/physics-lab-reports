
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10, 10))
plt.minorticks_on()


x_1 = [10, 20, 34, 42, 49, 56]
y_1 = [382, 376, 372, 369, 367, 364]

coef_1 = np.polyfit(x_1,y_1,1)  #approximation
poly1d_fn = np.poly1d(coef_1) 
plt.plot(x_1, poly1d_fn(x_1))



plt.xlim(0, 60)    #range
plt.ylim(350, 390) 

plt.grid(which='major') 


plt.plot(x_1, y_1, 'b--')  #show values
plt.plot(x_1, y_1, 'bs')

plt.ylabel(r'$P,  \ бар$')  #name axis
plt.xlabel(r'$T,  \ С$')

plt.grid(True)


plt.show()   

