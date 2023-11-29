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
