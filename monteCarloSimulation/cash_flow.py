import numpy as np

# Define parameters
num_iterations = 10000

# Historical cash flow data (in CHF)
cash_flow = np.array([1200, 1300, 1250, 1280, 1350, 1320, 1400, 1360, 1420, 1380, 1430, 1450])

# Compute mean and standard deviation for cash flow
mean_cash_flow = np.mean(cash_flow)
std_dev_cash_flow = np.std(cash_flow)

# Create empty list to hold total yearly cash flow simulations
total_cash_flow_simulations = []

for i in range(num_iterations):
    # Simulate cash flow for each month of the year and sum to get total yearly cash flow
    simulated_yearly_cash_flow = np.sum([np.random.normal(mean_cash_flow, std_dev_cash_flow) for _ in range(12)])

    # Append simulated yearly cash flow to list
    total_cash_flow_simulations.append(simulated_yearly_cash_flow)

# Convert list to numpy array
total_cash_flow_simulations = np.array(total_cash_flow_simulations)

# Compute mean total yearly cash flow
mean_yearly_cash_flow = np.mean(total_cash_flow_simulations)

# Compute percentiles for total yearly cash flow
cash_flow_5th_percentile = np.percentile(total_cash_flow_simulations, 5)
cash_flow_95th_percentile = np.percentile(total_cash_flow_simulations, 95)

print(f"Mean Yearly Cash Flow: CHF {mean_yearly_cash_flow:.2f}")
print(f"5th Percentile of Yearly Cash Flow: CHF {cash_flow_5th_percentile:.2f}")
print(f"95th Percentile of Yearly Cash Flow: CHF {cash_flow_95th_percentile:.2f}")
