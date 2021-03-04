import numpy as np

def solver(a,b):
    x = np.linalg.solve(a, b)
    print('x={}, y={}'.format(x[0],x[1]))

a = np.array([[4,5],[5,-8]])
b = np.array([10,11])

solver(a,b)
