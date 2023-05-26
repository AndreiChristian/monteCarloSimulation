import numpy as np
import matplotlib.pyplot as plt

rate = 3
num_values = 1000

poisson_values = np.random.poisson(rate, num_values)

plt.hist(poisson_values, bins = range(11), edgecolor='black',align='left', )
plt.xlabel('Number of Events')
plt.ylabel('Frequency')
plt.title('Poisson Distribution')
plt.show()