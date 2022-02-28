
from numpy import loadtxt
import matplotlib.pyplot as plt

data = loadtxt('outp2n12.dat')
t = data[:, 0]
x = data[:, 1]
xdelay = data[:, 24]

plt.figure(figsize=(7.5, 4)).subplots_adjust(bottom=0.12)

plt.xlabel('t')
plt.grid(True)

lw = 1.5
plt.plot(t, x, 'b', linewidth=lw, label=r'$x(t)$')
plt.plot(t, xdelay, 'g', linewidth=lw, label=r'$x(t-1)$')

plt.ylim(ymin=0.75, ymax=3.25)

plt.legend(framealpha=1, shadow=True, loc=(.56, .75))
plt.savefig('delay_plot_p2n12.svg', dpi=200, transparent=True)

# show()
