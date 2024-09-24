import numpy as np
import matplotlib.pyplot as plt


t, y = np.loadtxt('sdd.csv', unpack=True, skiprows=1, delimiter=',')

plt.figure(figsize=(7.5, 4)).subplots_adjust(bottom=0.12)

plt.xlabel('t')
plt.ylabel('y')
plt.title('State-Dependent Delay Example')
plt.grid(True)

plt.plot(t, y, 'bo', markersize=3.5, alpha=0.5)

lw = 1

t1 = [0, np.e - 1]
y1 = [t1[0]+1, t1[1]+1]
plt.plot(t1, y1, 'g', linewidth=lw)

t2 = np.linspace(np.e - 1, np.exp(2) - 1, 51)
y2 = np.exp((t2 + 1) / np.e)
plt.plot(t2, y2, 'g', linewidth=lw)

t3 = np.linspace(np.exp(2)-1, 10, 51)
y3 = (np.e/(3 - np.log(t3 + 1)))**np.e
plt.plot(t3, y3, 'g', linewidth=lw)

plt.ylim(ymin=0.0, ymax=60.0)

plt.legend((r'dde_solver', 'exact'), loc='upper left',
           numpoints=1, framealpha=1, shadow=True)
plt.savefig('sdd.svg', transparent=True)

# plt.show()
