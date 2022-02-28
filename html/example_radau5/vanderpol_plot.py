
# vanderpol_plot.py
#
# Plot the solution to the van der Pol system that was saved in vdp.dat.
# Save the plot in vanderpol_plot.svg.
#

from numpy import loadtxt
import matplotlib.pyplot as plt


t, x, y = loadtxt('vdp.dat', unpack=True)

plt.figure(1, figsize=(7.5, 4)).subplots_adjust(bottom=0.12)
plt.xlabel('t')
plt.grid(True)
lw = 1.5
plt.plot(t, x, 'b', linewidth=lw, label=r'$x$')
plt.plot(t, y, 'g--', linewidth=lw, label=r'$y$')
plt.legend(framealpha=1, shadow=True)
plt.title('van der Pol')
plt.savefig('vanderpol_plot.svg', dpi=200, transparent=True)

# plt.show()
