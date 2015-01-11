
from numpy import loadtxt
import matplotlib.pyplot as plt


data = loadtxt('rp.dat')
x = data[:,0]

plt.figure(1, figsize=(7.5, 6)).subplots_adjust(bottom=0.13, left=0.15)
plt.grid(True)
plt.hold(True)
lw = 1
plt.plot(x[:-1],x[1:], 'b.', linewidth=lw)
plt.xlabel(r'$x_i$', size=18)
plt.ylabel(r'$x_{i+1}$', size=18)
plt.title(r'Rossler System, x Return Map')
plt.axis('equal')
plt.xlim(-12.5, -3)
plt.ylim(-12.5, -3)
plt.savefig('rp_plot.png', dpi=200, transparent=True)
