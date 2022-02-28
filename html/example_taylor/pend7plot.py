
from numpy import loadtxt
import matplotlib.pyplot as plt


t, theta, v = loadtxt('pend7.dat', unpack=True)

plt.figure(figsize=(7.5, 4)).subplots_adjust(bottom=0.12)

plt.xlabel('t')
plt.grid(True)

lw = 1.5
plt.plot(t, theta, 'b', linewidth=lw, label=r'$\theta$')
plt.plot(t, v, 'g--', linewidth=lw, label=r'$v$')

plt.legend(framealpha=1, shadow=True)
plt.title('Damped Pendulum')
plt.savefig('pend7.svg', dpi=200, transparent=True)

# plt.show()
