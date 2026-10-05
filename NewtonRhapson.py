import numpy as np
import warnings

def my_func(x):
    return np.exp(0.7 * x) + 2 * x - 7

def my_func_derivative(x):
    return 0.7 * np.exp(0.7 * x) + 2

def newton_raphson(func, func_derivative, x_init, iter_lim, tol):
    iter_th = 0
    y = func(x_init)
    print(f'x_init = {x_init:.5f} | y = {y:.5f}')

    x = x_init
    while iter_th < iter_lim and np.abs(y) > tol:
        iter_th += 1
        print(f'iter_th = {iter_th} ---------------------------------------------------------')
        x = x - func(x) / func_derivative(x)
        y = func(x)
        print(f'x = {x:.7f} | y = {y}')

    if iter_th == iter_lim:
        warnings.warn(f'iteration number (={iter_th}) reaches the limit. The iteration may not convergence')

    return x, y, iter_th


def run_experiment(x_init, tol, iter_lim=50):
    x_sol, fx_sol, iter_num = newton_raphson(
        func=my_func, 
        func_derivative=my_func_derivative, 
        x_init=x_init, 
        iter_lim=iter_lim, 
        tol=tol
    )
    print(f'\n# With this parameter:')
    print(f'  x_init = {x_init}')
    print(f'  maximum iteration number = {iter_lim}')
    print(f'  tolerance = {tol}')
    print(f'# We get the following results:')
    print(f'  x_solution = {x_sol}')
    print(f'  the value of f(x) = {fx_sol}')
    print(f'  number of iteration = {iter_num}\n')


# Masukkan nilai parameter yang kamu inginkan langsung di sini:
x_init = 5
tol = 1e-3
iter_lim = 50

# Jalankan eksperimen
run_experiment(x_init=x_init, tol=tol, iter_lim=iter_lim)import numpy as np
import warnings

def my_func(R):
    return np.exp(-0.005 * R) * np.cos(0.05 * np.sqrt(2000 - 0.01 * R ** 2)) - 0.01

def my_func_derivative(R):
    return np.exp(-0.005 * R) * (
        -0.005 * np.cos(0.05 * np.sqrt(2000 - 0.01 * R**2))
        + 0.0005 * R * np.sin(0.05 * np.sqrt(2000 - 0.01 * R**2)) / np.sqrt(2000 - 0.01 * R**2)
    )

def newton_raphson(func, func_derivative, x_init, iter_lim, tol):
    iter_th = 0
    y = func(x_init)
    print(f'x_init = {x_init:.5f} | y = {y:.5f}')

    x = x_init
    while iter_th < iter_lim and np.abs(y) > tol:
        iter_th += 1
        print(f'iter_th = {iter_th} ---------------------------------------------------------')
        x = x - func(x) / func_derivative(x)
        y = func(x)
        print(f'x = {x:.7f} | y = {y}')

    if iter_th == iter_lim:
        warnings.warn(f'iteration number (={iter_th}) reaches the limit. The iteration may not convergence')

    return x, y, iter_th


def run_experiment(x_init, tol, iter_lim=50):
    x_sol, fx_sol, iter_num = newton_raphson(
        func=my_func, 
        func_derivative=my_func_derivative, 
        x_init=x_init, 
        iter_lim=iter_lim, 
        tol=tol
    )
    print(f'\n# With this parameter:')
    print(f'  x_init = {x_init}')
    print(f'  maximum iteration number = {iter_lim}')
    print(f'  tolerance = {tol}')
    print(f'# We get the following results:')
    print(f'  x_solution = {x_sol}')
    print(f'  the value of f(x) = {fx_sol}')
    print(f'  number of iteration = {iter_num}\n')


# Masukkan nilai parameter yang kamu inginkan langsung di sini:
x_init = 0
tol = 1e-3
iter_lim = 50

# Jalankan eksperimen
run_experiment(x_init=x_init, tol=tol, iter_lim=iter_lim)
