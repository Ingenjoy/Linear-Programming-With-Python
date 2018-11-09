# Linear-Programming-With-Python

Solving Linear Programming problems using Simplex Method with `linprog` from `scipy.optimize`, `NumPy` and `PuLP` libraries on Python.

## Linear Programming

Linear programming is used to solve optimization problems. In a LP problem must be defined an **Objective Function** and **Constraints**, and they must be **Strictly Linears**. Constraints may be equalities or inequalities.

### Example:

Variables:
<p align="center">
   <img src="https://latex.codecogs.com/png.latex?\center&space;x_{1}&space;=&space;chairs&space;\center&space;x_{2}&space;=&space;tables"/>
</p>
Objective Function:
<p align="center">
   <img src="https://latex.codecogs.com/png.latex?z(max)=5x_{1}&space;&plus;&space;4x_{2}"/></p>
Constraints:
<p align="center">
   <img src="https://latex.codecogs.com/png.latex?\center&space;C1&space;=&space;6x_{1}&space;&plus;&space;4x_{2}&space;\leq&space;24&space;\center&space;C2&space;=&space;x_{1}&space;&plus;&space;2x_{2}&space;\leq&space;6&space;\center&space;C3&space;=&space;-x_{1}&space;&plus;&space;x_{2}&space;\leq&space;1&space;\center&space;C4&space;=&space;x_{2}&space;\leq&space;2&space;\center&space;x_{1},&space;x_{2}&space;\geq&space;0"/></p>

## Requirement

We are going to use SciPy, NumPy and PuLP libraries to solve LP problems. PuLP is not available on Anaconda, try with `pip`.

Install via pip: 

    pip install scipy numpy pulp

Install via conda: 

    conda install scipy numpy

## Examples

### Using linprog from SciPy
* [Solving LP Problem](https://github.com/Gabeqb/Linear-Programming-With-Python/blob/master/notebooks/Linprog/LP-Problem01.ipynb "Problem01")

* [Solving Integer LP Problem](https://github.com/Gabeqb/Linear-Programming-With-Python/blob/master/notebooks/Linprog/LP-Problem02.ipynb "Problem02")

### Using PuLP
* [Solving LP Problem](https://github.com/Gabeqb/Linear-Programming-With-Python/blob/master/notebooks/PuLP/LP-Problem01.ipynb "Problem01")

* [Solving Integer LP Problem](https://github.com/Gabeqb/Linear-Programming-With-Python/blob/master/notebooks/PuLP/LP-Problem02.ipynb "Problem02")


## Company X Problem

[Solving Company X problem with Linprog](https://github.com/Gabeqb/Linear-Programming-With-Python/blob/master/notebooks/Linprog/CompanyX-Problem.ipynb)
[Solving Company X problem with PuLP](https://github.com/Gabeqb/Linear-Programming-With-Python/blob/master/notebooks/PuLP/CompanyX-Problem.ipynb)

![](notebooks/CompanyX.png)
