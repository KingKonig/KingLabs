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
uploaded_file = st.file_uploader("Upload a CSV", type="csv", accept_multiple_files=True)
if uploaded_file is not None:
    print(f"Selected File: {uploaded_file}")

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


if __name__ == "__main__":
    if uploaded_file is not None and st.button("Display Graphs"):
        # Vars for crop
        start = 0
        end = 100

        # Data processing
        data = kingfiles.file_processor(file=uploaded_file, export=True)
        data = kingfunky.na_dropper(data)
        data = kingfunky.data_cropper(data, start, end)

        # Plot the data
        plot()
