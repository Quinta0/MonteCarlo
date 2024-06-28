# MonteCarlo
## Monte Carlo Simulation to Estimate Pi

This program uses a Monte Carlo simulation to estimate the value of Pi. The program generates random points within a square of side length 2, centered at the origin, and calculates how many of those points fall inside a unit circle. The ratio of the points inside the circle to the total number of points is used to estimate Pi.

### How to Run

1. Make sure you have `numpy` and `matplotlib` installed, if not you can install them using the following command:
    ```bash
    pip install requirements.txt
    ```
2. Save the script as `pi.py`.
3. Run the script using the command `python pi.py` or `py pi.py` if you have installed python from the microsoft store.

### Output
The output is an animation of the Monte Carlo simulation and a GIF file named PI.gif saved in the same directory.


## Portfolio Analysis with Real Stock Data
This program performs a Monte Carlo simulation to analyze the potential future returns of a portfolio composed of real stocks. Historical data is fetched from Yahoo Finance.

### How to Run
1. Make sure you have `numpy`, `pandas`, `matplotlib`, and `yfinance` installed, just as before if dont have them installed you can install them with the following command:
```bash
pip install requirements.txt
```
2. Save the script as `portfolio.py`.
3. Run the script using the command `python portfolio.py` or `py pi.py` if you have installed python from the microsoft store.