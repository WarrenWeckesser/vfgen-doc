
from numpy import loadtxt
import matplotlib.pyplot as plt


t, theta, v = loadtxt('pend_taylor_demo_gsl.csv', unpack=True, skiprows=1, delimiter=',')
ts, theta3, v3, theta7, v7, theta15, v15 = loadtxt('pend_taylor_samples.csv',
                                                   unpack=True, skiprows=1, delimiter=',')

plt.figure(figsize=(7.5, 4)).subplots_adjust(bottom=0.12)

plt.xlabel('t')
plt.ylabel(r'$\theta$')
plt.grid(True)

lw = 1.5
plt.plot(t, theta, 'k', linewidth=lw, label='GSL')
plt.plot(ts, theta3, ':', linewidth=lw, label='Order 3')
plt.plot(ts, theta7, '-.', linewidth=lw, label='Order 7')
plt.plot(ts, theta15, '--', linewidth=lw, label='Order 15')
plt.xlim(0, 1.0)
plt.ylim(-0.75, 1.25)

plt.legend(framealpha=1, shadow=True, loc='lower left')

plt.savefig('pend_taylor_demo.svg', dpi=200, transparent=True)
# plt.show()
