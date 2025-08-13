import io
import datetime
from typing import List, Optional

# Matplotlib is used for plotting the chart
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# The 'tool' decorator from the Google ADK library
from google.adk.tools import tool

@tool
def plot_stock_prices(
    prices: List[float],
    ticker: str,
    dates: Optional[List[datetime.date]] = None
) -> bytes:
    """
    Generates a line chart of stock prices and returns it as a PNG image.

    This optimized tool can plot prices against their corresponding dates for a more
    accurate time-series representation. It also handles cases with no data gracefully.

    Args:
        prices: A list of stock prices.
        ticker: The stock ticker symbol.
        dates: An optional list of dates corresponding to each price point.

    Returns:
        A PNG image of the line chart, or an empty bytes object if no data is provided.
    """
    # Return an empty object if no price data is provided to prevent an error
    if not prices:
        print("Warning: No price data provided to plot.")
        return b''

    # Use plt.subplots() for better control over the figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))

    # Check if dates are provided and match the length of prices
    if dates and len(dates) == len(prices):
        # FIX: The following line explicitly converts date objects to datetime objects
        # to satisfy the Pylance type checker, which can be overly strict.
        datetime_objects = [datetime.datetime.combine(d, datetime.time.min) for d in dates]
        ax.plot(datetime_objects, prices, marker='o', linestyle='-')

        # Format the x-axis to handle dates nicely
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())
        fig.autofmt_xdate()  # Auto-rotate date labels for better readability
        ax.set_xlabel("Date")
    else:
        # If no dates, plot against a simple numerical index
        ax.plot(prices, marker='o', linestyle='-')
        ax.set_xlabel("Time (Sequential Data Points)")

    # Set chart titles and labels
    ax.set_title(f"{ticker} Stock Price History")
    ax.set_ylabel("Price (USD)")
    ax.grid(True)  # Add a grid for easier value reading

    # Ensure the plot layout is clean and nothing is cut off
    plt.tight_layout()

    # Save the plot to an in-memory buffer
    buf = io.BytesIO()
    try:
        plt.savefig(buf, format='png')
        buf.seek(0)
        return buf.getvalue()
    finally:
        # IMPORTANT: Close the figure to free up memory
        plt.close(fig)