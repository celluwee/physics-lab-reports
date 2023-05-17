import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10, 10))
plt.minorticks_on()


y1 = [137, 278, 415, 553, 693, 840, 973, 1113, 1260]
y2 = [156, 315, 470, 624, 785, 947, 1104, 1258, 1423]
y3 = [181, 363, 546, 727, 912, 1091, 1276, 1457, 1641]
y4 = [200, 405, 602, 812, 1007, 1217, 1414, 1625, 1820]
n = [1, 2, 3, 4, 5, 6, 7, 8, 9]


plt.xlim(0, 10) 
plt.ylim(120, 2000) 

plt.grid(which='major')




coef_1 = np.polyfit(n,y1,1) 
poly1d_fn = np.poly1d(coef_1) 
plt.plot(n, poly1d_fn(n), 'b')

coef_2 = np.polyfit(n,y2,1) 
poly1d_fn = np.poly1d(coef_2)  
plt.plot(n, poly1d_fn(n), 'r')


coef_3 = np.polyfit(n,y3,1) 
poly1d_fn = np.poly1d(coef_3) 
plt.plot(n, poly1d_fn(n), 'g')

coef_4 = np.polyfit(n,y4,1) 
poly1d_fn = np.poly1d(coef_4) 
plt.plot(n, poly1d_fn(n), 'k')



plt.plot(n, y1, 'bo')
plt.plot(n, y2, 'ro')
plt.plot(n, y3, 'go')
plt.plot(n, y4, 'ko')
plt.ylabel(r'$ν,  \ Hz$')
plt.xlabel(r'$n$')

plt.grid(True)

plt.legend([r'$f_1(n)=140,0*n-4.22$', r'$f_2(n)=158.13*n-3.78$', r'$f_3(n)=182.43*n-1.72$', r'$f_4(n)=202.817*n-2.75$'], loc=2)


plt.show()

