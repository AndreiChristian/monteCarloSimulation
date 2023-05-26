import numpy as np

data = [7,9,14,12,9,10]

np_data = np.array(data)

# standard deviation
std_deviation = np.std(np_data)

# variance
variance = np.var(np_data)

# range
range = np.ptp(np_data)

'''Interquartile Range (IQR): 
The IQR is a measure of variability that considers the spread of the middle 50% of the data. 
It is calculated as the difference between the third quartile (Q3) and the first quartile (Q1) and 
is less sensitive to extreme values compared to the range.'''

Q1 = np.percentile(np_data,25)
Q3 = np.percentile(np_data,75)
iqr = Q3 - Q1


'''Coefficient of Variation (CV): 
The CV is a relative measure of variability that expresses the standard deviation as a percentage of the mean. 
It is useful when comparing the variability of different datasets with different means.'''

cv = (np.std(data) / np.mean(data)) * 100

'''Skewness:
 Skewness measures the asymmetry of a distribution. 
 Positive skewness indicates a longer tail on the right side of the distribution, 
 while negative skewness indicates a longer tail on the left side. 
 Skewness helps understand the departure from symmetry in the data.'''


'''Kurtosis: 
Kurtosis measures the shape of the distribution and describes the presence of heavy tails or sharp peaks. 
High kurtosis indicates a distribution with heavy tails, while low kurtosis indicates a distribution with 
lighter tails compared to a normal distribution.'''

print("Standard deviation : ", std_deviation)
print("Variance : ", variance)
print("Range : ", range)
print("Interquartile Range (IQR):", iqr)
print("Coefficient of Variation (CV):", cv)
