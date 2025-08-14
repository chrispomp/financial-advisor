import base64
from io import BytesIO
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns  # Import seaborn
from google.adk.tools import FunctionTool

def plot_data_seaborn(data: dict, title: str, x_label: str, y_label: str) -> dict:
    """Generates a highly aesthetic line chart using seaborn.

    Args:
        data: The data to plot.
        title: The title of the chart.
        x_label: The label for the x-axis.
        y_label: The label for the y-axis.

    Returns:
        A dictionary containing the base64 encoded image of the chart.
    """
    df = pd.DataFrame(data)
    
    # Set the seaborn theme and style
    sns.set_theme(style="whitegrid", palette="viridis")
    
    plt.figure(figsize=(10, 6))
    
    # Use seaborn's lineplot for a more aesthetic plot
    # It automatically selects nice colors and adds confidence intervals if data allows
    sns.lineplot(data=df, x=df.columns[0], y=df.columns[1], marker='o', linewidth=2.5)
             
    plt.title(title, fontsize=18, weight='bold')
    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=12)
    
    plt.tight_layout()
    
    buffer = BytesIO()
    plt.savefig(buffer, format="png", dpi=100)
    buffer.seek(0)
    
    encoded_image = base64.b64encode(buffer.read()).decode("utf-8")
    
    plt.close()
    
    return {
        "image": encoded_image
    }

charting = FunctionTool(plot_data_seaborn)

# --- Example Usage ---
# sample_data = {
#     'Date': pd.to_datetime(['2025-01-01', '2025-02-01', '2025-03-01', '2025-04-01', '2025-05-01']),
#     'Portfolio Value': [500, 525, 510, 550, 580]
# }
# chart_output = plot_data_seaborn(sample_data, 'Portfolio Growth YTD', 'Date', 'Portfolio Value (K$)')
# print("Seaborn chart generated successfully.")