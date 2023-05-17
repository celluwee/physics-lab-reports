import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10, 10))
plt.minorticks_on()

plt.grid(which='major')

plt.grid(which='minor', linestyle=':')
x = [0.5 , 1, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14.5, 15.5, 16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20.5, 21.5, 22.5]
y = [0.1, 0.04, 0.08, 0.08, 0.09, 0.1, 0.17, 0.2, 0.35, 2, 1.16, 0.62, 0.32, 0.3, 0.24, 0.24, 0.24, 0.36, 0.14, 0.24, 0.22, 0.3, 0.5, 2.06, 2.42, 0.94, 0.38, 0.2, 0.32, 0.12, 0.19, 0.06, 0.06]
plt.plot(x, y)
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.xlabel(r'$V$')
plt.ylabel(r'$ΔpH/ΔV$')
plt.yticks(np.arange(0, 3, .5))
plt.title(r'$Differential \ titration \ curve\ H_3PO_4$')
plt.grid(True)

plt.show()