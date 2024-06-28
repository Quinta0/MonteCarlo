import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample historical return data (in real use, replace with actual data)
data = {
    'Asset1': np.random.normal(0.01, 0.02, 1000),
    'Asset2': np.random.normal(0.015, 0.025, 1000),
    'Asset3': np.random.normal(0.02, 0.03, 1000),
}

returns = pd.DataFrame(data)

# Calculate mean returns and covariance matrix
mean_returns = returns.mean()
cov_matrix = returns.cov()

# Portfolio weights (assuming an equally weighted portfolio)
weights = np.array([1 / 3, 1 / 3, 1 / 3])

# Number of simulations
num_simulations = 100000

# Time horizon (e.g., 252 trading days in a year)
time_horizon = 252

# Initialize arrays to store simulation results
simulated_portfolio_returns = np.zeros(num_simulations)

# Run Monte Carlo simulations
for i in range(num_simulations):
    # Generate random returns for each asset
    random_returns = np.random.multivariate_normal(mean_returns, cov_matrix, time_horizon)

    # Calculate portfolio return for each time period
    portfolio_returns = np.dot(random_returns, weights)

    # Calculate cumulative return over the time horizon
    cumulative_return = np.prod(1 + portfolio_returns) - 1

    # Store the cumulative return in the results array
    simulated_portfolio_returns[i] = cumulative_return

# Plot the distribution of simulated portfolio returns
plt.hist(simulated_portfolio_returns, bins=50, edgecolor='k', alpha=0.7)
plt.title('Distribution of Simulated Portfolio Returns')
plt.xlabel('Cumulative Return')
plt.ylabel('Frequency')
plt.show()

# Summary statistics
mean_simulated_return = np.mean(simulated_portfolio_returns)
std_dev_simulated_return = np.std(simulated_portfolio_returns)
var_95 = np.percentile(simulated_portfolio_returns, 5)

print(f"Mean Simulated Return: {mean_simulated_return:.2%}")
print(f"Standard Deviation of Simulated Return: {std_dev_simulated_return:.2%}")
print(f"Value at Risk (95% confidence level): {var_95:.2%}")
