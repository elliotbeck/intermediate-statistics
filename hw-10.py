## Rice, Exercise 8.6c)

# Import libraries
import numpy as np
from math import comb
import matplotlib.pyplot as plt

# Define parameters
p = 0.5
n = 10


# Define the log-likelihood function
def loglik(x, p, n):
    return x * np.log(p) + (n - x) * np.log(1 - p) + np.log(comb(n, x))


# Plot log-likelihood for each value of p
p_grid = np.arange(0.01, 1, 0.01)
log_lik_values = [loglik(5, p, n) for p in p_grid]
plt.plot(p_grid, log_lik_values)
plt.vlines(
    p_grid[np.argmax(log_lik_values)],
    ymax=np.max(log_lik_values),
    ymin=np.min(log_lik_values),
    linestyles="dashed",
    color="red",
)
plt.xticks(np.arange(0, 1.1, 0.1))
plt.xlabel("p")
plt.ylabel("log-likelihood")
plt.show()
# The maximum likelihood estimate for p is 5/10 = 0.5

## Wolf Exercise 2
# Create data
data = np.array(
    [
        [-2.2, -0.2, 0.2, 1.2, -0.2, 0.4, 0.1],
        [-0.5, 0.7, -0.4, 0.3, 0.7, 1.2, -0.3],
        [0.4, -0.9, 0.1, 0.8, -1.1, -0.6, 0.5],
        [0.7, 1.8, -0.2, 0.7, -1.2, 1.9, -1.1],
    ]
)

# Calculate the grand mean and shrinkage mean estimator for various alphas
grand_mean = np.mean(np.mean(data, axis=1))
alphas = [0, 0.25, 0.5, 0.75, 1]
mean_shrinkage = [
    alpha * grand_mean + (1 - alpha) * np.mean(data, axis=1) for alpha in alphas
]

## Wolf Exercise 3
# Find the optimal alpha according to Stein, Page 38, Slides 08
sigma_hat = (1 / (data.shape[0] - 1)) * np.sum((data.T - np.mean(data, axis=1)) ** 2)
alpha_star = (
    (data.shape[0] - 3) * sigma_hat / np.sum((data.T - np.mean(data, axis=1)) ** 2)
)

# Calculate the shrinkage mean estimator for the optimal alpha
mean_shrinkage_optimal = alpha_star * grand_mean + (1 - alpha_star) * np.mean(
    data, axis=1
)
