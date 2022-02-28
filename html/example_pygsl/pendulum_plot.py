
from numpy import loadtxt
import matplotlib.pyplot as plt


t, theta, v, energy = loadtxt('pend.dat', unpack=True)

plt.figure(1, figsize=(7.5, 4)).subplots_adjust(bottom=0.12)
plt.xlabel('t')
plt.grid(True)
plt.plot(t, theta, 'b', label=r'$\theta$')
h = plt.plot(t, v, 'g--', label=r'$v$')
plt.plot(t, energy, 'r-.', label='energy')
plt.ylim(-10, 11)
plt.legend(framealpha=1, shadow=True)
plt.title('Damped Pendulum')
plt.savefig('pendplot.svg', transparent=True)

# plt.show()
