import numpy as np
import scipy.stats as stats

delivery_times = [28, 29, 31, 32, 30, 29, 28, 33, 30, 31, 32, 29, 30, 29, 31, 30, 31, 30, 28, 29]

sample_mean = np.mean(delivery_times)
sample_std = np.std(delivery_times)
sample_size = len(delivery_times)

confidence_level = 0.95
alpha = 1 - confidence_level
critical_value = stats.t.ppf(1 - alpha/2, df=sample_size-1)

margin_of_error = critical_value * (sample_std / np.sqrt(sample_size))

lower_bound = sample_mean - margin_of_error
upper_bound = sample_mean + margin_of_error

print("Sample Mean:", sample_mean)
print("Margin of Error:", margin_of_error)
print("Confidence Interval:", (lower_bound, upper_bound))
