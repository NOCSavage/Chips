import numpy as np
import matplotlib.pyplot as plt
import warnings


def function(x) : 
    return np.exp(-0.5 * x) - 0.1 * x - 0.5

x_low = float(input("lower x = "))
x_up = float(input("upper x = "))
iter_lim = int(input("maximum iteration = "))
tol = float(input("tolerance = "))

def bisection(func, x_low, x_up, iter_lim, tol, verbose=True): 
    assert x_low < x_up, "Error, x_low must be lower than x_up !"

    assert func(x_low) * func(x_up) < 0 

    if verbose :
        print("BISECTION METHOD")
        print("\nFunction :")
        print("f(x) = exp(-0.5 * x) - 0.1 * x - 0.5")

        print("\nInitial Conditions :")
       
        print("\nStopping Criteria")
        print("|f(x) < tolerance|")

    iter_0 = 0
    x_root = x_low + (x_up - x_low) / 2
    y_root = function(x_root)
    while iter_0 < iter_lim and abs(y_root) > tol:
        iter_0 += 1

        print(f"* Iteration {iter_0}")
        
       
    if np.sign(func(x_root)) == np.sign(func(x_low)):
            x_low = x_root
            print(f'Based on the signs, current x_root becomes x_low')
    else:
            x_up = x_root
            print(f'Based on the signs, current x_root becomes x_up')

    x_root = x_low + (x_up - x_low) / 2  # update x_root using the bisection method
    y_root = func(x_root)
    print(f'x_low = {x_low:.5f} | x_root = {x_root:.5f} | x_up = {x_up:.5f} | y_root = {y_root:.5f}')

    if iter_0 == iter_lim:
        warnings.warn(f'iteration number (={iter_0}) reaches the limit. The iteration may not convergence')

    return x_root, y_root

    x_solution, y_solution = bisection(func=function, x_low= id(x_low) , x_up= id(x_up), iter_lim=id(iter_lim), tol=id(tol))
    print(f'THE SOLUTION TO THE ROOT OF EQUATION PROBLEM: x = {x_sol_assignment}')
