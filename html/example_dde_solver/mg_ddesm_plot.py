
from numpy import loadtxt
import matplotlib.pyplot as plt


t, x = loadtxt('mg.dat', unpack=True)

plt.figure(figsize=(8, 4)).subplots_adjust(bottom=0.12)

plt.xlabel('t')
plt.ylabel('x')
plt.title('Mackey-Glass Delay Equation Solution')
plt.grid(True)

lw = 1.5
plt.plot(t, x, 'b', linewidth=lw)

plt.savefig('mg.svg', transparent=True)

# plt.show()
