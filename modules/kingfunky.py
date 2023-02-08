# Imports
import matplotlib.pyplot as plt
import streamlit as st


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


def auto_plot(frame_list):
    # Get amount of plots
    n_graphs = len(frame_list)

    # Setup plot figure
    if n_graphs < 3:
        n_columns = n_graphs
    else:
        n_columns = 3

    if n_graphs % n_columns == 0:
        n_rows = n_graphs // n_columns
    else:
        n_rows = (n_graphs // n_columns) + 1

    plt.style.use("dark_background")
    fig, axs = plt.subplots(n_rows, n_columns, figsize=(n_columns * 5, n_rows * 5))

    # Plot
    current_row = 0
    current_column = 0

    for frame in frame_list:
        if current_column > n_columns - 1:
            current_row += 1
            current_column = 0

        axs[current_row, current_column].plot(
            frame.iloc[:, 0].to_list(),
            frame.iloc[:, 1].to_list(),
        )

        header = frame.columns.values.tolist()[1]
        axs[current_row, current_column].set_title(header)

        print(f"Plot {header} completed.")

        current_column += 1

    return fig
