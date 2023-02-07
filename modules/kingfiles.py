# Imports
import pandas as pd


# Functions
def frame_read(file_list):
    """
    Reads a list of CSV files

    :return: Pandas dataframe
    """

    # Setup dataframe
    df = pd.DataFrame()

    # Read the file to dataframe
    for file in file_list:
        file_df = pd.read_csv(file, delimiter=",")

        df = pd.concat([df, file_df], axis=1)

    # Sets index to be [0,n]
    df = df.reset_index()

    return df


def list_read(file_list):
    """
    Reads a list of CSV files

    :return: Pandas dataframe
    """

    # Setup list for dataframes
    df_list = []

    # Read the file to dataframe
    for file in file_list:
        file_df = pd.read_csv(file, delimiter=",")

        df_list.append(file_df)

    return df_list


def file_processor(file_list=None, columns=None, interpolate=False, export=False):
    """
    Reads a CSV file selected by the user with the file browser.

    Column list example: ["frame_no", "timestamp", "rx-green", "ry-green"]

    :param interpolate:
    :param file_list: file from Streamlit
    :param export: Exports a csv if True
    :param columns: a list of columns desired
    :return: Pandas dataframe with specified columns
    """

    # Read list of files
    if file_list is not None:
        df_list = list_read(file_list)

    else:
        raise Exception(
            f"File processor died"
        )

    # Selects columns to keep
    if columns is not None:
        for i, df in enumerate(df_list):
            df_list[i] = df[columns]

    if interpolate:
        for i, df in enumerate(df_list):
            df_list[i] = df.interpolate(method="linear", axis=0)

    if export:
        for i, df in enumerate(df_list):
            df.to_csv(f"data-file_processor{i}.csv", index=False)

    return df_list
