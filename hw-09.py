# Plots of the MSEs of the ML and MoM estimators for the uniform distribution
# as a function of the sample size n are shown below.
# Import packages
import numpy as np
import matplotlib.pyplot as plt


# Define MSE of uniform ML estimator for a given sample size and theta
def mse_uniform_mle(n, theta):
    return (2 * theta**2) / ((n + 1) * (n + 2))


# Define MSE of uniform MoM estimator for a given sample size and theta
def mse_uniform_mom(n, theta):
    return (theta**2) / (3 * n)


# Plot MSE of uniform ML estimator for a given theta and sample size range
def plot_mse_uniform_mle(theta, n_range):
    # Compute MSE for each sample size
    mse_mle = [mse_uniform_mle(n, theta) for n in n_range]
    mse_mom = [mse_uniform_mom(n, theta) for n in n_range]
    # Plot MSE as a function of sample size
    plt.plot(n_range, mse_mle, label="MSE of ML estimator")
    plt.plot(n_range, mse_mom, label="MSE of MoM estimator")
    plt.xlabel("Sample size")
    plt.ylabel("MSE")
    plt.title("MSEs of estimators for uniform distribution with theta=" + str(theta))
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # Define sample size range
    n_range = np.arange(1, 500, 1)
    # Define theta (try other values)
    theta = 1
    # Plot MSE of uniform ML estimator for a given theta and sample size range
    plot_mse_uniform_mle(theta, n_range)
