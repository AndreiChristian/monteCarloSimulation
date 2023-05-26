import numpy as np

# Define parameters
num_iterations = 10000

# Revenue data (in CHF per month)
competitors_revenue_burgers = np.array([3500, 4000, 3200, 3700, 3900])
competitors_revenue_hotdogs = np.array([2200, 2500, 2000, 2300, 2400])
competitors_revenue_sodas = np.array([1400, 1500, 1300, 1600, 1450])

# Expense data (in CHF per month)
rent_expense = np.array([800, 1000, 900, 950, 850])
ingredients_expense = np.array([2000, 2200, 2100, 2300, 2050])
utilities_expense = np.array([400, 500, 450, 500, 400])
salaries_expense = np.array([2000, 2200, 2100, 2250, 2150])

loan_interest_expense = np.array([200, 220, 210, 215, 205])  # New expense

# Compute mean and standard deviation for all revenue sources and expenses
mean_values = [np.mean(arr) for arr in [competitors_revenue_burgers, competitors_revenue_hotdogs, competitors_revenue_sodas, 
                                        rent_expense, ingredients_expense, utilities_expense, salaries_expense, loan_interest_expense]]
std_dev_values = [np.std(arr) for arr in [competitors_revenue_burgers, competitors_revenue_hotdogs, competitors_revenue_sodas, 
                                          rent_expense, ingredients_expense, utilities_expense, salaries_expense, loan_interest_expense]]

# Create empty lists to hold results
revenue_simulations = []
profit_simulations = []

for i in range(num_iterations):
    # Simulate revenue and expenses
    simulated_values = [np.random.normal(mean_values[j], std_dev_values[j]) for j in range(8)]
    simulated_revenue = sum(simulated_values[0:3])
    simulated_expense = sum(simulated_values[3:])
    simulated_profit = simulated_revenue - simulated_expense
    
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
