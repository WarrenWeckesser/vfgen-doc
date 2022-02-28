
from numpy import loadtxt
import matplotlib.pyplot as plt


vdp8 = loadtxt('vdp8.dat')
vdp8_t = vdp8[:, 0]
vdp8_x = vdp8[:, 1]

vdpgsl = loadtxt('vdpgsl.dat')
vdpgsl_t = vdpgsl[:, 0]
vdpgsl_x = vdpgsl[:, 1]


plt.figure(figsize=(7.5, 4)).subplots_adjust(bottom=0.12)

plt.xlabel('t')
plt.ylabel('x')
plt.grid(True)

lw = 1.5

plt.plot(vdp8_t, vdp8_x, 'b', linewidth=1.25,
         alpha=0.6, label=r'Adaptive Taylor, Order 8')
plt.plot(vdpgsl_t, vdpgsl_x, 'g--', linewidth=2,
         alpha=0.6, label=r'GSL (rk8pd)')

plt.legend(framealpha=1, shadow=True, loc='best')
plt.title('Van der Pol Equation')
plt.xlim(8.5, 10)
plt.ylim(-2.2, 3.3)
plt.savefig('vdp8compare.svg', dpi=200, transparent=True)

# plt.show()
