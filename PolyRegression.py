import numpy as np
import matplotlib.pyplot as plt

np.random.seed(seed=42)

w0_true = 1.5
w1_true = 0.7
w2_true = 0.1
w3_true = -0.02
w4_true = 0.001
noise_variance = 0.25

x = np.linspace(start=0.0, stop=10.0, num=11)
noise_std = np.sqrt(noise_variance)
noise = np.random.normal(loc=0.0, scale=noise_std, size=x.shape)

y_clean = (
    w0_true
    + w1_true * x
    + w2_true * x**2
    + w3_true * x**3
    + w4_true * x**4
)

y = y_clean + noise

print(f"x: {x}")
print(f"noise_std: {noise_std}")
print(f"noise: {noise}")
print(f"y: {y}")
print(f"y_clean: {y_clean}")

N = 4  # polynomial degree
M = len(x)  # number of data
M = np.size(x)
X = np.zeros(shape=(M, N + 1))

print(f"N: {N}")
print(f"M: {M}")
print(f"X.shape: {X.shape}")
print(f"X:\n{X}")

for i in range(M):
    print(f"i={i} ------------------")
    X[i, 0] = 1.0       # column 0
    X[i, 1] = x[i]      # column 1
    X[i, 2] = x[i]**2   # column 2
    X[i, 3] = x[i]**3   # column 3
    X[i, 4] = x[i]**4   # column 4

print(f"X (setelah for-loop):\n{X}")

w = np.linalg.inv(X.T @ X) @ X.T @ y
print(f"w:\n{w}")



y_hat = (
    w[0]
    + w[1] * x
    + w[2] * x**2
    + w[3] * x**3
    + w[4] * x**4
)

plt.scatter(x, y, color="tab:orange", label="noisy labels")
plt.plot(x, y_clean, color="tab:blue", label="clean labels")
plt.plot(x, y_hat, color="tab:green", label="predicted labels")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
