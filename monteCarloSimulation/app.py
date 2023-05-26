import numpy as np

# Define the range of possible revenue and expense values
revenue_range = [1000000, 1500000]  # Example: Revenue between 1,000,000 and 1,500,000
expense_range = [500000, 800000]  # Example: Expense between 500,000 and 800,000

# Define the number of simulations
num_simulations = 10000

# Generate random values for revenue and expense using uniform distribution
revenue_values = np.random.uniform(revenue_range[0], revenue_range[1], num_simulations)
expense_values = np.random.uniform(expense_range[0], expense_range[1], num_simulations)

# Calculate gross profit for each simulation
gross_profit_values = revenue_values - expense_values

# Analyze the distribution of gross profit values
min_gross_profit = np.min(gross_profit_values)
max_gross_profit = np.max(gross_profit_values)
mean_gross_profit = np.mean(gross_profit_values)

# # Print the summary statistics of gross profit
# print("Summary Statistics of Gross Profit:")
# print("Minimum Gross Profit: ", min_gross_profit)
# print("Maximum Gross Profit: ", max_gross_profit)
# print("Mean Gross Profit: ", mean_gross_profit)

print(revenue_values)