
from numpy import loadtxt
import matplotlib.pyplot as plt


t, theta, v = loadtxt('demo_gsl.csv', unpack=True, skiprows=1, delimiter=',')
t3, theta3, v3 = loadtxt('demo3.csv', unpack=True, skiprows=1, delimiter=',')
t7, theta7, v7 = loadtxt('demo7.csv', unpack=True, skiprows=1, delimiter=',')
t15, theta15, v15 = loadtxt('demo15.csv', unpack=True, skiprows=1, delimiter=',')

plt.figure(figsize=(7.5, 4)).subplots_adjust(bottom=0.12)

plt.xlabel('t')
plt.ylabel(r'$\theta$')
plt.grid(True)

lw = 1.5
plt.plot(t, theta, 'k', linewidth=lw, label='GSL')
plt.plot(t3, theta3, ':', linewidth=lw, label='Order 3')
plt.plot(t7, theta7, '-.', linewidth=lw, label='Order 7')
plt.plot(t15, theta15, '--', linewidth=lw, label='Order 15')
plt.xlim(0, 1.0)
plt.ylim(-0.75, 1.25)

plt.legend(framealpha=1, shadow=True, loc='lower left')

plt.savefig('pend_taylor_demo.svg', dpi=200, transparent=True)
# plt.show()
