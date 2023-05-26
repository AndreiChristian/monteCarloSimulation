import numpy as np

# Define parameters
num_iterations = 10000

# Information provided by competitors
competitors_revenue_icecream = np.array([2000, 2300, 1900, 2200, 2100])
competitors_revenue_lemonade = np.array([800, 1000, 900, 1100, 950])
competitors_revenue_water = np.array([500, 550, 600, 500, 450])

rent_expense = np.array([400, 700, 500, 600, 300])
electricity_expense = np.array([150, 200, 180, 220, 160])
icecream_expenses = np.array([300,200,150,400,200])

# Compute mean and standard deviation for all revenue sources and expenses
revenue_icecream_mean = np.mean(competitors_revenue_icecream)
revenue_icecream_std_dev = np.std(competitors_revenue_icecream)

revenue_lemonade_mean = np.mean(competitors_revenue_lemonade)
revenue_lemonade_std_dev = np.std(competitors_revenue_lemonade)

revenue_water_mean = np.mean(competitors_revenue_water)
revenue_water_std_dev = np.std(competitors_revenue_water)

rent_mean = np.mean(rent_expense)
rent_std_dev = np.std(rent_expense)

electricity_mean = np.mean(electricity_expense)
electricity_std_dev = np.std(electricity_expense)

icecream_mean = np.mean(icecream_expenses)
icecream_std_dev = np.std(icecream_expenses)

# Create empty lists to hold results
revenue_simulations = []
profit_simulations = []

for i in range(num_iterations):
    # Simulate revenue and expenses
    simulated_revenue_icecream = np.random.normal(revenue_icecream_mean, revenue_icecream_std_dev)
    simulated_revenue_lemonade = np.random.normal(revenue_lemonade_mean, revenue_lemonade_std_dev)
    simulated_revenue_water = np.random.normal(revenue_water_mean, revenue_water_std_dev)
    simulated_rent = np.random.normal(rent_mean, rent_std_dev)
    simulated_electricity = np.random.normal(electricity_mean, electricity_std_dev)
    simulated_icecream_cost = np.random.normal(icecream_mean, icecream_std_dev)
    
    # Total simulated revenue and expense
    simulated_revenue = simulated_revenue_icecream + simulated_revenue_lemonade + simulated_revenue_water
    simulated_expense = simulated_rent + simulated_electricity + simulated_icecream_cost

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

# Desired profit
desired_profit = 2750

# Calculate probability of achieving the desired profit
prob_of_desired_profit = np.sum(profit_simulations >= desired_profit) / num_iterations

print(f"Probability of achieving at least CHF {desired_profit}: {prob_of_desired_profit * 100:.2f}%")
