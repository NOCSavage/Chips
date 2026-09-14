import numpy as np
import matplotlib.pyplot as plt
import warnings


def function(x):
    return np.exp(-0.5 * x) - 0.1 * x - 0.5


def bisection(x_low, x_up, iter_lim, tol):

    assert x_low < x_up, "x_low must be lower than x_up!"
    assert function(x_low) * function(x_up) < 0, \
        "Root is not between x_low and x_up!"

    iteration = 0

    while iteration < iter_lim:

        x_root = x_low + (x_up - x_low) / 2
        y_root = function(x_root)

        iteration += 1

        print(
            f"Iteration {iteration}: "
            f"x_low = {x_low:.6f}, "
            f"x_root = {x_root:.6f}, "
            f"x_up = {x_up:.6f}, "
            f"f(x) = {y_root:.6f}"
        )

        if abs(y_root) <= tol:
            break

        if function(x_low) * y_root < 0:
            x_up = x_root
        else:
            x_low = x_root

    if iteration == iter_lim and abs(y_root) > tol:
        warnings.warn("Maximum iteration reached.")

    return x_root, y_root


# Input
x_low = float(input("Lower x = "))
x_up = float(input("Upper x = "))
iter_lim = int(input("Maximum iteration = "))
tol = float(input("Tolerance = "))


# Bisection
x_solution, y_solution = bisection(
    x_low, x_up, iter_lim, tol
)


# Result
print("\nFINAL RESULT")
print(f"x    = {x_solution:.10f}")
print(f"f(x) = {y_solution:.10f}")


# Plot
x = np.linspace(x_low, x_up, 500)

plt.plot(x, function(x))
plt.axhline(0)
plt.axvline(x_solution, linestyle="--")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Bisection Method")
plt.grid()
plt.show()