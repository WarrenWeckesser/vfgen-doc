
from numpy import loadtxt
import matplotlib.pyplot as plt


data = loadtxt('mg.dat')
t = data[:, 0]
x = data[:, 1]
xdelay = data[:, 74]

plt.figure(figsize=(7.5, 4)).subplots_adjust(bottom=0.12)

plt.xlabel('t')
plt.grid(True)

lw = 1.5
plt.plot(t, x, 'b', linewidth=lw, label=r'$x(t)$')
plt.plot(t, xdelay, 'g', linewidth=lw, label=r'$x(t-17)$')

plt.ylim(ymin=0.0, ymax=1.4)

plt.legend(framealpha=1, shadow=True, loc='lower right')
plt.savefig('mg.svg', dpi=200, transparent=True)

# show()
