# File:   pend7plot.py
# Author: Warren Weckesser, https://warrenweckesser.github.io

from numpy import loadtxt
import matplotlib.pyplot as plt


t, theta, v = data = loadtxt('pend7.csv', unpack=True, delimiter=',', skiprows=1)

plt.figure(1, figsize=(7.5, 4)).subplots_adjust(bottom=0.12)
plt.xlabel('t')
plt.grid(True)
lw = 1.5
plt.plot(t, theta, 'b', linewidth=lw, label=r'$\theta$')
plt.plot(t, v, 'g', linewidth=lw, label=r'$v$')
plt.legend(framealpha=1, shadow=True)
plt.title('Damped Pendulum')
plt.savefig('pend7.svg', transparent=True)

# plt.show()
