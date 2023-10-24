# Import libraries
import numpy as np

# Two assets with given mu and sigma
# We will create a portfolio with these two assets

mu = np.array([1, 0.8])


def cov_matrix(rho):
    return np.array([[0.1**2, rho * 0.1 * 0.12], [rho * 0.1 * 0.12, 0.12**2]])


def mu_sigma(weight, mu_vec, cov_mat):
    mu = np.dot(weight, mu_vec)
    sigma = np.sqrt(np.dot(weight.T, np.dot(cov_mat, weight)))
    return mu, sigma


# Plot the efficient frontier
import matplotlib.pyplot as plt


def efficient_frontier(rho):
    # Let's create a list of weights
    weight_list = []
    for w in np.arange(0, 1.01, 0.01):
        weight_list.append(np.array([w, 1 - w]))

    # Let's get the mu and sigma for each weight
    mu_list = []
    sigma_list = []
    for weight in weight_list:
        return_portfolio, sigma = mu_sigma(weight, mu, cov_matrix(rho))
        mu_list.append(return_portfolio)
        sigma_list.append(sigma)
    return mu_list, sigma_list


mu_list, sigma_list = efficient_frontier(1)

# Plot the efficient frontier
plt.plot(sigma_list, mu_list)
# Add the assets to the plot
plt.scatter(0.1, 1)
plt.scatter(0.12, 0.8)
plt.show()
