"""A tool for generating charts."""
import base64
from io import BytesIO
import matplotlib.pyplot as plt
import pandas as pd
from google.adk.tools import FunctionTool

def plot_data(data: dict, title: str, x_label: str, y_label: str) -> dict:
    """Generates a line chart from the given data and returns it as a base64 encoded string.

    Args:
        data: The data to plot.
        title: The title of the chart.
        x_label: The label for the x-axis.
        y_label: The label for the y-axis.

    Returns:
        A dictionary containing the base64 encoded image of the chart.
    """

    df = pd.DataFrame(data)
    plt.figure(figsize=(10, 6))
    plt.plot(df.iloc[:, 0], df.iloc[:, 1])
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    
    encoded_image = base64.b64encode(buffer.read()).decode("utf-8")
    
    return {
        "image": encoded_image
    }

charting = FunctionTool(plot_data)