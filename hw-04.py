# Import libraries
import numpy as np

# Let's look at the hat problem
# Each person has one hat, in total we have n hats
# Each person randomly picks a hat

# We will repeat this experiment for n = 2, 5, 100, 1000
for n in [2, 5, 100, 1000]:
    # Each time we will count the number of matches
    # The probability of a match is 1 divided by n, for each person
    # We will repeat this 100000 times
    matches_list = []
    for i in range(10000):
        # Let's create a list of n hats
        hats = np.arange(n)

        # Let's create a list of n people
        people = np.arange(n)

        # Let's randomly shuffle the hats
        np.random.shuffle(hats)

        # Let's count the number of matches
        matches = np.sum(hats == people)

        # Let's store the number of matches
        matches_list.append(matches)
    print("n = ", n, "mean = ", np.mean(matches_list), "std = ", np.std(matches_list))

# Expected number of matches is 1
# Standard deviation is 1, we didn't show that in class
