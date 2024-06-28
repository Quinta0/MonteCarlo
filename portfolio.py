import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Define the list of stock tickers and the portfolio weights
tickers = ['AAPL', 'MSFT', 'GOOGL']
weights = np.array([0.3, 0.4, 0.3])  # Example weights, should sum to 1

# Fetch historical data for the tickers
data = yf.download(tickers, start="2020-01-01", end="2023-01-01")['Adj Close']

# Calculate daily returns
returns = data.pct_change().dropna()

# Calculate mean returns and covariance matrix
mean_returns = returns.mean()
cov_matrix = returns.cov()

# Number of simulations
num_simulations = 10000

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
