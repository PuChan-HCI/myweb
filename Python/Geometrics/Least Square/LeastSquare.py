import numpy as np
from scipy.optimize import leastsq

x = np.array([100, 300, 590, 90, 310, 550, 105, 290, 560])
y = np.array([100, 110, 115, 250, 240, 230, 400, 380, 390])
z = np.array([40, 512, 1024, 40, 512, 1024, 40, 512, 1024])

def func(params, x, y, z):
    a, b, c, d, e, f = params[0], params[1], params[2], params[3], params[4], params[5]
    residual = z-(a*x**2 + b*y**2 + c*x*y + d*x + e*y + f)
    return residual

params = [0, 0, 0, 0, 0, 0]
result = leastsq(func, params, (x, y, z))
print(result)