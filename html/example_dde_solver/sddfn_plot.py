import numpy as np
import matplotlib.pyplot as plt


t, y = np.loadtxt('sddfn.dat', unpack=True)

plt.figure(figsize=(7.5, 4)).subplots_adjust(bottom=0.12)

plt.xlabel('t')
plt.ylabel('y')
plt.title('State-Dependent Delay Example: Feldstein-Neves')
plt.grid(True)

plt.plot(t, y, 'bo', markersize=3.5, alpha=0.5)

lw = 1

t1 = np.linspace(0, 1.0, 51)
y1 = np.sqrt(t1 + 1)
plt.plot(t1, y1, 'g', linewidth=lw)

t2 = np.linspace(1.0, 2.0, 51)
y2 = (t2 + 1)/4 + 0.5 + (1 - np.sqrt(2.0)/2)*np.sqrt(t2 + 1)
plt.plot(t2, y2, 'g', linewidth=lw)

# plt.xlim(xmin=0.0, xmax=2.0)
plt.ylim(ymin=0.95, ymax=1.8)

plt.legend((r'dde_solver', 'exact'), loc='upper left',
           numpoints=1, framealpha=1, shadow=True)
plt.savefig('sddfn.svg', transparent=True)

# plt.show()
