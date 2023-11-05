# Coding example CLT
# Import libraries
import numpy as np
from scipy.stats import poisson, norm
import matplotlib.pyplot as plt

# Let's define the parameters, we use the poisson distribution
# mu is the mean and sigma is the standard deviation of the poisson distribution
# Note: mu = sigma**2 for the poisson distribution
mu = 2
sigma = 2**0.5
n_sim = 10000
n_sample = 10  # 10 is small, increase it to see what happens!

# Let's generate n_sim mean values each based on n_sample poisson random variables
mean_list = []
for i in range(n_sim):
    mean_list.append(np.mean(poisson.rvs(mu, size=n_sample)))

# Let's normalize the mean values
mean_list = (np.array(mean_list) - mu) / (sigma / n_sample**0.5)

# Let's plot a histogram of the mean values and compare it to the normal standard normal
x = np.linspace(-5, 5, 1000)
plt.plot(x, norm.pdf(x, loc=0, scale=1), label="Standard normal distribution")
plt.hist(mean_list, bins=30, density=True, label="Histogram of means")
plt.legend()
plt.show()
# Play around with the sample size (n_sample) and see how the magic happens!
