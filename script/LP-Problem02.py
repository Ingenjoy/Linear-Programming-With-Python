from scipy.optimize import linprog
import numpy as np

# Objective function
z = np.array([ 7, 6])

# Constraints
C = np.array([
    [ 2, 3],          #C1
    [ 6, 5]           #C2
])

b = np.array([12, 30])

# Bounds
x1 = (0, None)
x2 = (0, None)

#Solution
sol = linprog(-z, A_ub = C, b_ub = b, bounds = (x1, x2), method='simplex', options={'maxiter':True})

print(f"x1 = {sol.x[0]}, x2 = {sol.x[1]}, z = {sol.fun*-1}")