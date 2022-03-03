
from numpy import loadtxt
import matplotlib.pyplot as plt


t, theta, v, energy = loadtxt('pend.dat', unpack=True)

plt.figure(1, figsize=(7.5, 4)).subplots_adjust(bottom=0.12)

plt.plot(t, theta, label=r'$\theta$')
plt.plot(t, v, '--', label=r'$v$')
plt.plot(t, energy, '-.', label='energy')

plt.title('Damped Pendulum')
plt.xlabel('t')
plt.grid(True)
plt.legend(framealpha=1, shadow=True)

plt.savefig('pendulum_plot.svg', dpi=200, transparent=True)

# plt.show()
