import numpy as np
import matplotlib.pyplot as plt

# Example: Analysis of Test Scores using the Normal Distribution

# Context: Imagine you are a teacher assessing the performance of your students in a recent test. 
# You want to understand the distribution of test scores and see if they follow a normal pattern.

# Simulated test scores of a class
test_scores = np.array([85, 92, 78, 88, 95, 80, 90, 87, 84, 92, 96, 79, 85, 88, 91, 87, 83, 89, 94, 90])

# Calculate mean and standard deviation of the test scores
mean = np.mean(test_scores)
std_dev = np.std(test_scores)

# Generate a range of scores using the normal distribution
scores_range = np.linspace(mean - 3 * std_dev, mean + 3 * std_dev, 100)

# Calculate the probability density function (PDF) using the normal distribution
pdf = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((scores_range - mean) / std_dev) ** 2)

# Plot the histogram of test scores
plt.hist(test_scores, bins=10, edgecolor='black', alpha=0.5, density=True, label='Test Scores')

# Plot the normal distribution curve
plt.plot(scores_range, pdf, color='red', label='Normal Distribution')

plt.xlabel('Test Scores')
plt.ylabel('Frequency')
plt.title('Distribution of Test Scores')
plt.legend()
plt.grid(False)
plt.show()
