# Imports
from modules import kingfiles, kingstats, kingfunky
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stat
import numpy as np
import streamlit as st

# Main
# Prepare Data ---------------------------------------------------------------------------------------------------------

# File upload widget
uploaded_file_list = st.file_uploader("Upload a CSV", type="csv", accept_multiple_files=True)
# if uploaded_file_list is not None:
#     print(f"Selected File(s): {uploaded_file_list}")

# Select columns
# columns = [
#     "Time(seconds)",
#     "Load Cell (lbf)",
#     "Run Tank Pressure (psig)",
#     "Combustion Chamber Pressure (psig)",
# ]

# Calcs ----------------------------------------------------------------------------------------------------------------


# Plots ----------------------------------------------------------------------------------------------------------------
def plot():
    plt.style.use("dark_background")
    fig, axs = plt.subplots(2, 2)
    plt.subplots_adjust(wspace=0.5, hspace=0.5)

    # Example:
    # # Time vs Load Cell
    # axs[0, 0].plot(
    #     data["Time(seconds)"],
    #     data["Load Cell (lbf)"],
    #     c="green"
    # )

    # Web GUI
    st.title("SET Data")
    st.pyplot(fig)


def auto_plot(df):
    # Get headers of dataset
    headers = df.columns.values.tolist()

    # Iterate to find how many graphs are needed
    n_graphs = 0
    skip_list = ["index", "frame_no", "timestamp"]

    for header in headers:
        if header in skip_list:
            continue
        n_graphs += 1

    # Setup plot figure
    n_columns = 3
    if n_graphs % n_columns == 0:
        n_rows = n_graphs // n_columns
    else:
        n_rows = (n_graphs // n_columns) + 1

    plt.style.use("dark_background")
    fig, axs = plt.subplots(n_rows, n_columns, figsize=(n_columns * 5, n_rows * 5))
    # plt.subplots_adjust(wspace=0.5, hspace=0.5)

    # Grab values for x axis
    x_axis = df["timestamp"]

    # Plot
    current_row = 0
    current_column = 0

    for header in headers:
        if header in skip_list:
            continue

        if current_column > n_columns - 1:
            current_row += 1
            current_column = 0

        axs[current_row, current_column].plot(
            x_axis,
            df[header],
        )

        axs[current_row, current_column].set_title(header)

        print(f"Plot {header} completed.")

        current_column += 1

    # Send to streamlit
    st.pyplot(fig)


if __name__ == "__main__":
    if uploaded_file_list is not None and st.button("Display Graphs"):
        # Vars for crop
        start = 0
        end = 100

        # Data processing
        data = kingfiles.file_processor(uploaded_file_list, export=True)
        data = kingfunky.na_dropper(data, threshold=100, export=True)

        # Plot the data
        # plot()
        auto_plot(data)
