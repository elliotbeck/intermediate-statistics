# Coding example for Rice 4.72 (Branching processes)
# Import libraries
import numpy as np
from scipy.stats import poisson

# Let's define the parameters, we use the poisson distribution
# mu is the mean and sigma is the standard deviation of the poisson distribution
# Note: mu = sigma**2 for the poisson distribution
mu = 2
sigma = 2**0.5
n_sim = 10000
n_gen = 3

# Let's simulate the branching process
# We will store the number of individuals in each generation in a list
n_list = []
for i in range(n_sim):
    total_population = 1
    for j in range(n_gen):
        family_sizes = poisson.rvs(mu, size=total_population)
        total_population = np.sum(family_sizes)

    n_list.append(total_population)

# Let's calculate mean and standard error
mean = np.mean(n_list)
variance = np.var(n_list, ddof=1)

# Theoretical mean and variance derived in the lecture
theoretical_mean = mu**n_gen
theoretical_variance = (sigma**2 * mu ** (n_gen - 1)) * ((1 - mu**n_gen) / (1 - mu))

# Print all results
print("Mean: " + str(np.round(mean, 2)))
print("Theoretical mean: " + str(np.round(theoretical_mean, 2)))
print("Variance: " + str(np.round(variance, 2)))
print("Theoretical variance: " + str(np.round(theoretical_variance, 2)))
# Seems to be a good approximation!
