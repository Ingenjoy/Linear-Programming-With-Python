# Linear-Programming-With-Python
Solving Linear Programming problems using Simplex Method with `linprog` from `scipy.optimize` and `numpy` libraries on Python.

## Linear Programming.
Linear programming is used to solve optimization problems. In a LP problem must be defined an **Objective Function** and **Constraints**, and they must be **Strictly Linears**. Constraints may be equalities or inequalities.

### Example:

Variables:
<p align="center">
   <img src="https://latex.codecogs.com/png.latex?\center&space;x_{1}&space;=&space;chairs&space;\center&space;x_{2}&space;=&space;tables" title="\center x_{1} = chairs \center x_{2} = tables" />
</p>
Objective Function:
<p align="center">
   <img src="https://latex.codecogs.com/png.latex?z(max)=5x_{1}&space;&plus;&space;4x_{2}" title="z(max)=5x_{1} + 4x_{2}" /></p>
Constraints:
<p align="center">
   <img src="https://latex.codecogs.com/png.latex?\center&space;C1&space;=&space;6x_{1}&space;&plus;&space;4x_{2}&space;\leq&space;24&space;\center&space;C2&space;=&space;x_{1}&space;&plus;&space;2x_{2}&space;\leq&space;6&space;\center&space;C3&space;=&space;-x_{1}&space;&plus;&space;x_{2}&space;\leq&space;1&space;\center&space;C4&space;=&space;x_{2}&space;\leq&space;2&space;\center&space;x_{1},&space;x_{2}&space;\geq&space;0" title="\center C1 = 6x_{1} + 4x_{2} \leq 24 \center C2 = x_{1} + 2x_{2} \leq 6 \center C3 = -x_{1} + x_{2} \leq 1 \center C4 = x_{2} \leq 2 \center x_{1}, x_{2} \geq 0" /></p>

## Requirement
We are going to use, Scipy and Numpy libraries to solves LP problems.

Installing via pip: 

    pip3 install scipy numpy

Installing via conda: 

    conda install scipy numpy

## Solutions

[Solving LP Problem](https://github.com/Gabeqb/Linear-Programming-With-Python/blob/master/notebooks/Linear%20Programming.ipynb "Test")

**Solving Integer LP Problem**
