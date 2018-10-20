from scipy.optimize import linprog
import numpy as np

# Objective function
z = np.array([300,500,200])
expense = 75000

# Constraints
C = np.array([
    [ 10, 7.5,   4],        #C1
    [  0,  10,   0],        #C2
    [0.5, 0.4, 0.5],        #C3
    [  0, 0.4,   0],        #C4
    [0.5, 0.1, 0.5],        #C5
    [0.4, 0.2, 0.4],        #C6
    [  1, 1.5, 0.5],        #C7
    [  1,   0,   0],        #C8
    [  0,   1,   0],        #C9
    [  0,   0,   1]         #C10
])

b = np.array([4350, 2500, 280, 140, 280, 140, 700, 300, 180, 400])

# Bounds
x1 = (0, None)
x2 = (0, None)
x3 = (0, None)

#Solution
sol = linprog(-z, A_ub = C, b_ub = b, bounds = (x1, x2, x3), method='simplex')

#Profit Monthly.
profit = (sol.fun*-1) - expense

print(f"x1 = {sol.x[0]}, x2 = {sol.x[1]}, x3 = {sol.x[2]}, z = {profit}")