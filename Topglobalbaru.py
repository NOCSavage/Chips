import numpy as np
import matplotlib.pyplot as plt
import warnings


def function(x):
    return np.exp(-0.5 * x) - 0.1 * x - 0.5


def bisection(func, x_low, x_up, iter_lim, tol, verbose=True):

    assert x_low < x_up, \
        "Error, x_low must be lower than x_up!"

    assert func(x_low) * func(x_up) < 0, \
        "Error, root is not between x_low and x_up!"

    if verbose:
        print("BISECTION METHOD")

        print("\nFunction :")
        print("f(x) = exp(-0.5 * x) - 0.1 * x - 0.5")

        print("\nInitial Conditions :")
        print(f"lower x = {x_low}")
        print(f"upper x = {x_up}")
        print(f"maximum iteration = {iter_lim}")
        print(f"tolerance = {tol}")

        print("\nStopping Criteria")
        print("|f(x_root)| <= tolerance")

    iter_0 = 0

    x_root = x_low + (x_up - x_low) / 2
    y_root = func(x_root)

    while iter_0 <= iter_lim and abs(y_root) > tol:

        iter_0 += 1

        if verbose:
            print(f"\n* Iteration {iter_0}")

        if np.sign(func(x_root)) == np.sign(func(x_low)):
            x_low = x_root

            if verbose:
                print("Based on the signs, current x_root becomes x_low")

        else:
            x_up = x_root

            if verbose:
                print("Based on the signs, current x_root becomes x_up")

        x_root = x_low + (x_up - x_low) / 2
        y_root = func(x_root)

        if verbose:
            print(
                f"x_low = {x_low:.5f} | "
                f"x_root = {x_root:.5f} | "
                f"x_up = {x_up:.5f} | "
                f"y_root = {y_root:.5f}"
            )

    if iter_0 == iter_lim and abs(y_root) > tol:
        warnings.warn(
            f"iteration number (={iter_0}) reaches the limit."
        )

    return x_root, y_root


# INPUT DARI TERMINAL
x_low = float(input("lower x = "))
x_up = float(input("upper x = "))
iter_lim = int(input("maximum iteration = "))
tol = float(input("tolerance = "))


# MENJALANKAN BISECTION
x_solution, y_solution = bisection(
    func=function,
    x_low=x_low,
    x_up=x_up,
    iter_lim=iter_lim,
    tol=tol,
    verbose=True
)


# HASIL AKHIR
print("\nTHE SOLUTION TO THE ROOT OF EQUATION PROBLEM:")
print(f"x = {x_solution:.10f}")
print(f"f(x) = {y_solution:.10f}")


# PLOT
x = np.linspace(x_low, x_up, 500)
y = function(x)

plt.plot(x, y, linewidth=3)
plt.axhline(y=0, linewidth=2, color="k")
plt.axvline(x=x_solution, linewidth=2, linestyle="--")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Bisection Method")
plt.grid(True)

plt.show()