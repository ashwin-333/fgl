import matplotlib.pyplot as plt
import numpy as np


def plot_results(results, lookback_windows, forecasting_horizons):
    """
    Plot the Gaussian NLL Loss vs Forecasting Horizon for different lookback windows.
    """
    for lb in lookback_windows:
        plt.figure(figsize=(10, 6))
        plt.plot(forecasting_horizons, results[lb], marker='o', label=f"Lookback={lb}")
        plt.title(f"Gaussian NLLL vs Forecasting Horizon (Lookback={lb})")
        plt.xlabel("Forecasting Horizon")
        plt.ylabel("Gaussian NLLL Loss")
        plt.xticks(forecasting_horizons)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

def plot_uncertainty(preds, calibrated_preds, true_values, lower_bound, upper_bound, forecasting_horizon, lookback_window):

    plt.figure(figsize=(12, 6))
    plt.plot(true_values, label="True Values", color="blue", )
    plt.plot(preds, label="Original Predictions", color="green")
    #plt.plot(calibrated_preds, label="Calibrated Predictions", color="orange")

    plt.fill_between(range(len(preds)), 
                lower_bound,
                upper_bound,
                color='orange', alpha=0.2, label='Uncertainty Band')
    plt.legend()
    plt.xlabel("Time Step")
    plt.ylabel("Value")
    plt.title(f"Calibrated Predictions with Uncertainty Visualization (FH: {forecasting_horizon} LB: {lookback_window})")
    plt.legend()
    plt.show()
