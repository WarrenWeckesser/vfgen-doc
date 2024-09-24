import numpy as np

data = np.loadtxt('rp.csv', skiprows=1, delimiter=',')
x = data[:, 0]
x0 = x[:-1]
x1 = x[1:]
np.savetxt('rp_x_return_map.csv', np.column_stack((x0, x1)),
           header="x, xnext", comments ='', delimiter=', ')
