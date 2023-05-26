import numpy as np

# Define the target profit value
target_profit = 400000  # Example: Target profit of 1,000,000

# Define the number of simulations
num_simulations = 100000

# Define the range for revenue and expense
revenue_range = (800000, 1200000)  # Example: Revenue range of 800,000 to 1,200,000
expense_range = (500000, 700000)   # Example: Expense range of 500,000 to 700,000

# Generate revenue and expense values for each simulation (based on your assumptions)
revenue_values = np.random.uniform(revenue_range[0], revenue_range[1], num_simulations)
expense_values = np.random.uniform(expense_range[0], expense_range[1], num_simulations)

# Calculate the gross profit for each simulation
gross_profit_values = revenue_values - expense_values

# Count the number of simulations where the profit meets or exceeds the target value
num_successful_simulations = np.sum(gross_profit_values >= target_profit)

# Calculate the percentage of simulations that achieve the target profit
percentage_successful = (num_successful_simulations / num_simulations) * 100

# Print the result
print(f"Percentage of simulations with a profit of {target_profit} or more: {percentage_successful:.2f}%")
