# Imports
import pandas as pd


# Functions
def read_files(file_list):
    """
    Reads a list of CSV files

    :return: Pandas dataframe
    """

    # Setup dataframe
    df = pd.DataFrame()

    # Read the file to dataframe
    for file in file_list:
        file_df = pd.read_csv(file, delimiter=",")

        df = pd.concat([df, file_df])

    # Sets index to be [0,n]
    df = df.reset_index()

    return df


def file_processor(file_list=None, columns=None, export=False):
    """
    Reads a CSV file selected by the user with the file browser.

    Column list example: ["frame_no", "timestamp", "rx-green", "ry-green"]

    :param file_list: file from Streamlit
    :param export: Exports a csv if True
    :param columns: a list of columns desired
    :return: Pandas dataframe with specified columns
    """

    # Read file or file path
    if file_list is not None:
        df = read_files(file_list)

    else:
        raise Exception(
            f"File processor died"
        )

    # Selects columns to keep
    if columns is not None:
        df = df[columns]

    if export:
        df.to_csv("Data.csv", index=False)

    return df
