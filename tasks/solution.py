# Task 1: Importing Numpy library
import numpy as np

# Task 2: Reading TXT file into a Numpy DataFrame called "score_data"
score_data = np.genfromtxt('data/scores.txt', delimiter=',')

# Task 3: Finding the Maximum score and store it in "score_max"
score_max = np.max(score_data)
print(score_max)

# Task 3: Finding the Minimum score and store it in "score_min"
score_min = np.min(score_data)
print(score_min)