# Import libraries
import numpy as np
from scipy.stats import cauchy, norm
from matplotlib import pyplot as plt

# Plot the densities
fig, ax = plt.subplots(1, 1)
x = np.linspace(cauchy.ppf(0.01), cauchy.ppf(0.99), 100)
ax.plot(
    x, cauchy.pdf(x, scale=0.5), "m-", lw=1, alpha=0.6, label="cauchy pdf, scale=0.5"
)
ax.plot(x, cauchy.pdf(x, scale=1), "r-", lw=1, alpha=0.6, label="cauchy pdf, scale=1")
ax.plot(x, cauchy.pdf(x, scale=2), "g-", lw=1, alpha=0.6, label="cauchy pdf, scale=2")
ax.plot(x, cauchy.pdf(x, scale=3), "y-", lw=1, alpha=0.6, label="cauchy pdf, scale=3")
ax.plot(x, norm.pdf(x), "b-", lw=1, alpha=0.6, label="normal pdf")
ax.legend(loc="best")
ax.grid()
plt.show()
# Both are symmetric, bell-shaped distributions, but the Cauchy distribution
# has much heavier tails than the normal distribution.
