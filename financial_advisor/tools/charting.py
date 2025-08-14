import base64
from io import BytesIO
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from google.adk.tools import FunctionTool

def generate_chart(data: dict, chart_type: str, title: str, x_label: str = "", y_label: str = "") -> dict:
    """
    Generates a chart of a specified type using seaborn.

    Args:
        data: The data to plot.
        chart_type: The type of chart to generate ('line', 'bar', or 'pie').
        title: The title of the chart.
        x_label: The label for the x-axis (optional).
        y_label: The label for the y-axis (optional).

    Returns:
        A dictionary containing the base64 encoded image of the chart or an error message.
    """
    try:
        df = pd.DataFrame(data)
        sns.set_theme(style="whitegrid", palette="viridis")
        plt.figure(figsize=(10, 6))

        if chart_type == 'line':
            if x_label and y_label:
                sns.lineplot(data=df, x=x_label, y=y_label, marker='o', linewidth=2.5)
            else:
                sns.lineplot(data=df, marker='o', linewidth=2.5)
        elif chart_type == 'bar':
            if x_label and y_label:
                sns.barplot(data=df, x=x_label, y=y_label)
            else:
                sns.barplot(data=df)
        elif chart_type == 'pie':
            if y_label and x_label:
                plt.pie(df[y_label], labels=df[x_label].tolist(), autopct='%1.1f%%', startangle=140)
            else:
                plt.pie(df.iloc[:, 1], labels=df.iloc[:, 0].tolist(), autopct='%1.1f%%', startangle=140)
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        else:
            return {"error": "Invalid chart type specified. Please choose 'line', 'bar', or 'pie'."}

        plt.title(title, fontsize=18, weight='bold')
        if x_label:
            plt.xlabel(x_label, fontsize=12)
        if y_label and chart_type != 'pie':
            plt.ylabel(y_label, fontsize=12)

        plt.tight_layout()

        buffer = BytesIO()
        plt.savefig(buffer, format="png", dpi=100)
        buffer.seek(0)

        encoded_image = base64.b64encode(buffer.read()).decode("utf-8")

        plt.close()

        return {"image": encoded_image}

    except Exception as e:
        return {"error": f"An error occurred during chart generation: {e}"}

charting = FunctionTool(generate_chart)