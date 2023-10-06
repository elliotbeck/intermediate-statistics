# Import libraries
from matplotlib import pyplot as plt
import numpy as np

# Define density function


def f(x, a=0.2):
    return (1/a) * x**(-(1+a)/a)


# Plot for various a
x = np.linspace(0.01, 0.1, 1000)
for a in [0.5, 0.55, 0.6]:
    plt.plot(x, f(x, a), label='a={}'.format(a))
    plt.legend()
    plt.grid()
plt.show()

x = np.linspace(0.01, 0.5, 1000)
for a in [100, 200, 300, 400, 500]:
    plt.plot(x, f(x, a), label='a={}'.format(a))
    plt.legend()
    plt.grid()
plt.show()

# The rates of decrease of the tails seem to be the same for all a
