# Imports
import matplotlib.pyplot as plt
from modules import kingstats
import numpy as np


# Functions
def data_cropper(df, start, end, export=False):
    rows_to_delete = list()

    for i in range(len(df)):
        if df.iloc[i, 0] < start:
            rows_to_delete.append(i)

        if df.iloc[i, 0] > end:
            rows_to_delete.append(i)

    df = df.drop(df.index[rows_to_delete], index=None)

    if export:
        df.to_csv("data-data_cropper.csv", index=False)

    return df


def na_dropper(df, threshold=None, export=False):
    """
    Drops any row with missing data and drops columns that don't hit the threshold

    :param export:
    :param df: any pandas dataframe
    :param threshold: minimum amount of data points for a column if the threshold is 0 then no columns with be dropped
    :return: cleaned pandas dataframe
    """

    if threshold is not None:
        df.dropna(axis=1, thresh=threshold, inplace=True)

    df.dropna(axis=1, thresh=1, inplace=True)
    df.dropna(axis=0, how="any", inplace=True)

    if export:
        df.to_csv("data-na_dropper.csv", index=False)

    return df


# def butter_lowpass(cutoff, sample_rate, order=5):
#     return butter(order, cutoff, fs=sample_rate, btype='low', analog=False)
#
#
# def lowpass(data, cutoff, sample_rate, order):
#     b, a = butter_lowpass(cutoff, sample_rate, order=order)
#     y = lfilter(b, a, data)
#     return y


def auto_plot(df):
    # Get headers of dataset
    headers = df.columns.values.tolist()

    # Iterate to find how many graphs are needed
    n_graphs = 0
    skip_list = ["index", "frame_no", "timestamp", "x"]

    for header in headers:
        if header in skip_list:
            continue
        n_graphs += 1

    # Setup plot figure
    n_columns = 3
    if n_graphs % n_columns == 0:
        n_rows = n_graphs // n_columns
    elif n_graphs < n_columns:
        n_rows = 2
    else:
        n_rows = (n_graphs // n_columns) + 1

    plt.style.use("dark_background")
    fig, axs = plt.subplots(n_rows, n_columns, figsize=(n_columns * 10, n_rows * 10))
    # plt.subplots_adjust(wspace=0.5, hspace=0.5)

    # Grab values for x axis
    x_axis = df.iloc[:, 1]

    # Plot
    current_row = 0
    current_column = 0

    for header in headers:
        if header in skip_list:
            continue

        if current_column > n_columns - 1:
            current_row += 1
            current_column = 0

        # For moving average
        # n = 1000

        # For FFT
        delta_data_x = np.mean(np.diff(df[header]))
        fs = 1 / delta_data_x

        f_vec = np.fft.fftfreq(len(df[header]), 1 / fs)

        # define bounds for x
        axs[current_row, current_column].set_xlim([-0.1, 1])

        axs[current_row, current_column].plot(
            # Raw data
            # x_axis,
            # df[header],

            # Moving average
            # kingstats.moving_average(x_axis, n),
            # kingstats.moving_average(df[header], n),

            # Lowpass filter
            # x_axis,
            # kingstats.lowpassinator(x_axis, df[header]),

            # FFT
            f_vec,
            np.abs(np.fft.fft(df[header])),
            linewidth=1
        )

        axs[current_row, current_column].set_title(header)

        print(f"Plot {header} completed.")

        current_column += 1

    return fig
