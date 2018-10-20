from scipy.optimize import linprog
import numpy as np

# Objective function
z = np.array([5,4])

# Constraints
C = np.array([
    [1, 1],          #C1
    [10,6]           #C2
])

b = np.array([5,45])

# Bounds
x1 = (0, None)
x2 = (0, None)

#Solution
sol = linprog(-z, A_ub = C, b_ub = b, bounds = (x1, x2), method='simplex')

print(f"x1 = {sol.x[0]}, x2 = {sol.x[1]}, z = {sol.fun*-1}")