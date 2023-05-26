import numpy as np
import matplotlib.pyplot as plt

# Define the rate parameter (lambda) for the exponential distribution
rate = 0.5

# Generate random values from the exponential distribution
num_values = 1000
exponential_values = np.random.exponential(1/rate, num_values)

plt.hist(exponential_values, bins = 20, edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Exponential Distribution')
plt.show()