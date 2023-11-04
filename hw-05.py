# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Two assets with given mu and sigma
# We will create a portfolio with these two assets

mu = np.array([1, 0.8])


# Covariance matrix of the two assets with correlation rho (variance given)
def cov_matrix(rho):
    return np.array([[0.1**2, rho * 0.1 * 0.12], [rho * 0.1 * 0.12, 0.12**2]])


# Portfolio return and standard deviation
def mu_sigma(weight, mu_vec, cov_mat):
    mu = np.dot(weight, mu_vec)
    sigma = np.sqrt(np.dot(weight.T, np.dot(cov_mat, weight)))
    return mu, sigma


# Get mu und sigma of the portfolio for all weights
def mu_sigma_all_weights(rho):
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


# Plot the efficient frontier
mu_list, sigma_list = mu_sigma_all_weights(-0.5)
plt.plot(sigma_list, mu_list)
plt.grid()
plt.scatter(0.1, 1, label="Asset 1", color="red")
plt.scatter(0.12, 0.8, label="Asset 2", color="green")
plt.legend()
plt.show()
