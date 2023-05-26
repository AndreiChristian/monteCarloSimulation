import numpy as np

# Define parameters
num_iterations = 10000

# Historical sales data (in number of pizzas sold per year)
sales_margherita = np.array([1200, 1300, 1250, 1280, 1350])
sales_pepperoni = np.array([1500, 1600, 1550, 1520, 1620])
sales_vegetarian = np.array([800, 850, 820, 830, 860])

# Compute mean and standard deviation for each type of pizza sales
mean_sales_values = [np.mean(arr) for arr in [sales_margherita, sales_pepperoni, sales_vegetarian]]
std_dev_sales_values = [np.std(arr) for arr in [sales_margherita, sales_pepperoni, sales_vegetarian]]

# Define prices
prices = [10, 12, 11]  # in CHF

# Create empty list to hold revenue simulations
revenue_simulations = []

for i in range(num_iterations):
    # Simulate sales
    simulated_sales = [np.random.normal(mean_sales_values[j], std_dev_sales_values[j]) for j in range(3)]
    
    # Compute simulated revenue
    simulated_revenue = sum([simulated_sales[j] * prices[j] for j in range(3)])

    # Append simulated revenue to list
    revenue_simulations.append(simulated_revenue)

# Convert list to numpy array
revenue_simulations = np.array(revenue_simulations)

# Compute mean revenue
mean_revenue = np.mean(revenue_simulations)

# Compute percentiles for revenue
revenue_5th_percentile = np.percentile(revenue_simulations, 2.5)
revenue_95th_percentile = np.percentile(revenue_simulations, 97.5)

print(f"Mean Revenue: CHF {mean_revenue:.2f}")
print(f"5th Percentile of Revenue: CHF {revenue_5th_percentile:.2f}")
print(f"95th Percentile of Revenue: CHF {revenue_95th_percentile:.2f}")

# Desired revenue
desired_revenue = 40000

# Calculate probability of achieving the desired revenue
prob_of_desired_revenue = np.sum(revenue_simulations >= desired_revenue) / num_iterations

print(f"Probability of achieving at least CHF {desired_revenue}: {prob_of_desired_revenue * 100:.2f}%")
