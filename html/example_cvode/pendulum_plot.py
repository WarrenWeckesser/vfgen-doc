# File:   pendulum_plot.py
# Author: Warren Weckesser, https://warrenweckesser.github.io

from numpy import loadtxt
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


t, theta, v, energy = loadtxt('pend.dat', unpack=True)

plt.figure(figsize=(7.5, 4)).subplots_adjust(bottom=0.12)

plt.xlabel('t')
plt.grid(True)

lw = 1.5
plt.plot(t, theta, 'b', linewidth=lw)
plt.plot(t, v, 'g', linewidth=lw)
plt.plot(t, energy, 'r--', linewidth=lw)

plt.legend((r'$\theta$', r'$v$', 'energy'), prop=FontProperties(size=16))
plt.title('Damped Pendulum')
plt.savefig('pendplot.png', dpi=200, transparent=True)

# plt.show()
