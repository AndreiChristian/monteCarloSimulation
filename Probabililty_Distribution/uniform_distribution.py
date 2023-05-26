import numpy as np
import matplotlib.pyplot as plt

# Define the range for the uniform distribution
low = 0  # Lower bound
high = 10  # Upper bound

# Generate random values from the uniform distribution
num_values = 1000
uniform_values = np.random.uniform(low,high,num_values)

# Plot the histogram of the uniform distribution
plt.hist(uniform_values,bins = 20, edgecolor='black')
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Uniform Distribution")
plt.show()