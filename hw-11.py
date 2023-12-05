# Import libraries
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import poisson, nbinom

## Code for exercise 8.67
# Set up data
data = pd.DataFrame(
    {
        "counts": [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
        ],
        "beetles": [
            190,
            264,
            304,
            260,
            294,
            219,
            183,
            150,
            104,
            90,
            60,
            46,
            29,
            36,
            19,
            12,
            11,
            6,
            10,
            2,
            4,
            1,
            3,
            4,
            1,
            1,
            0,
            0,
            1,
        ],
        "glaux": [
            1,
            15,
            27,
            42,
            77,
            77,
            89,
            57,
            48,
            24,
            14,
            16,
            9,
            3,
            1,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
        ],
    }
)

# Create series from counts
glaux_observed = np.repeat(data["counts"].iloc[0:15], data["glaux"].iloc[0:15])
beetles_observed = np.repeat(data["counts"], data["beetles"])

# Fit poisson distribution using method of moments (E(X) = lambda)
lambda_glaux = np.mean(glaux_observed)
lambda_beetles = np.mean(beetles_observed)

# Fit negative binomial distribution using method of moments
# See: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.nbinom.html
# n is the number of successes, p is the probability of success
p_glaux = np.mean(glaux_observed) / np.var(glaux_observed)
n_glaux = np.mean(glaux_observed) ** 2 / (
    np.var(glaux_observed) - np.mean(glaux_observed)
)
p_beetles = np.mean(beetles_observed) / np.var(beetles_observed)
n_beetles = np.mean(beetles_observed) ** 2 / (
    np.var(beetles_observed) - np.mean(beetles_observed)
)

# Glaux maritima goodness of fit
x = list(range(0, data.counts.max() + 1))
plt.plot(x, poisson.pmf(x, lambda_glaux), label="Poisson")
plt.plot(x, nbinom.pmf(x, n_glaux, p_glaux), label="Negative binomial")
plt.hist(glaux_observed, density=True)
plt.legend()
plt.title("Glaux maritima goodness of fit")
plt.show()

# Potato beetles goodness of fit
plt.plot(x, poisson.pmf(x, lambda_beetles), label="Poisson")
plt.plot(x, nbinom.pmf(x, n_beetles, p_beetles), label="Negative binomial")
plt.hist(beetles_observed, density=True)
plt.title("Potato beetles goodness of fit")
plt.legend()
plt.show()

## Wolf Exercise 1
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

## Wolf Exercise 2
# Find the optimal alpha according to Stein, Page 38, Slides 08
sigma_hat = (1 / (data.shape[0] - 1)) * np.sum((data.T - np.mean(data, axis=1)) ** 2)
alpha_star = (
    (data.shape[0] - 3) * sigma_hat / np.sum((data.T - np.mean(data, axis=1)) ** 2)
)

# Calculate the shrinkage mean estimator for the optimal alpha
mean_shrinkage_optimal = alpha_star * grand_mean + (1 - alpha_star) * np.mean(
    data, axis=1
)
