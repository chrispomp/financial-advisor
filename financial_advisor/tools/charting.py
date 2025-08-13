"""Charting tools for financial advisor."""
import base64
import io
from typing import List, Optional

import matplotlib.pyplot as plt
import numpy as np
from google.adk.tools import FunctionTool
import datetime
import matplotlib.dates as mdates


def plot_stock_prices(
    prices: List[float], ticker: str, dates: Optional[List[str]] = None
) -> str:
    """
    Generates a line chart of stock prices and returns it as a PNG image.

    Args:
        prices: A list of stock prices.
        ticker: The stock ticker symbol.
        dates: An optional list of date strings, each in 'YYYY-MM-DD' format.

    Returns:
        A Base64-encoded string representing the PNG image of the line chart,
        or an empty string if no data is provided.
    """
    if not prices:
        print("Warning: No price data provided to plot.")
        return ""

    fig, ax = plt.subplots(figsize=(10, 6))
    plotted_with_dates = False
    if dates and len(dates) == len(prices):
        try:
            datetime_objects = [
                datetime.datetime.strptime(d_str, "%Y-%m-%d") for d_str in dates
            ]
            date_array = np.array(datetime_objects)
            ax.plot(date_array, prices, marker="o", linestyle="-")
            ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
            ax.xaxis.set_major_locator(mdates.AutoDateLocator())
            plt.gcf().autofmt_xdate()  # Auto-format dates
            ax.set_xlabel("Date")
            plotted_with_dates = True
        except ValueError:
            print(
                "Warning: Could not parse date strings. Defaulting to index-based plot."
            )

    if not plotted_with_dates:
        ax.plot(prices, marker="o", linestyle="-")
        ax.set_xlabel("Time (Sequential Data Points)")

    ax.set_title(f"{ticker} Stock Price History")
    ax.set_ylabel("Price (USD)")
    ax.grid(True)
    plt.tight_layout()

    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    image_bytes = buf.getvalue()
    base64_string = base64.b64encode(image_bytes).decode("utf-8")
    buf.close()
    plt.close(fig)

    return base64_string


plot_stock_prices_tool = FunctionTool(
    func=plot_stock_prices,
)