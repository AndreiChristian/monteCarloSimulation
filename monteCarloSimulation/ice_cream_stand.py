import numpy as np

# Define parameters
num_iterations = 10000

# Information provided by competitors
competitors_revenue = np.array([2000, 2300, 1900, 2200, 2100])
rent_expense = np.array([400, 700, 500, 600, 300])

# Compute mean and standard deviation for revenue and expense
revenue_mean = np.mean(competitors_revenue)
revenue_std_dev = np.std(competitors_revenue)
rent_mean = np.mean(rent_expense)
rent_std_dev = np.std(rent_expense)

# Create empty lists to hold results
revenue_simulations = []
profit_simulations = []

for i in range(num_iterations):
    
    # Simulate revenue and expense
    simulated_revenue = np.random.normal(revenue_mean, revenue_std_dev)
    simulated_rent = np.random.normal(rent_mean, rent_std_dev)
    simulated_profit = simulated_revenue - simulated_rent
    
    # Append results to lists
    revenue_simulations.append(simulated_revenue)
    profit_simulations.append(simulated_profit)

# Convert lists to numpy arrays
revenue_simulations = np.array(revenue_simulations)
profit_simulations = np.array(profit_simulations)

# Compute mean revenue and profit
mean_revenue = np.mean(revenue_simulations)
mean_profit = np.mean(profit_simulations)

# Compute percentiles for profit
profit_5th_percentile = np.percentile(profit_simulations, 5)
profit_95th_percentile = np.percentile(profit_simulations, 95)

print(f"Mean Revenue: CHF {mean_revenue:.2f}")
print(f"Mean Profit: CHF {mean_profit:.2f}")
print(f"5th Percentile of Profit: CHF {profit_5th_percentile:.2f}")
print(f"95th Percentile of Profit: CHF {profit_95th_percentile:.2f}")

# Desired profit
desired_profit = 1700

# Calculate probability of achieving the desired profit
prob_of_desired_profit = np.sum(profit_simulations >= desired_profit) / num_iterations

print(f"Probability of achieving at least CHF {desired_profit}: {prob_of_desired_profit * 100:.2f}%")
