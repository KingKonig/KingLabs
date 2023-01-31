# Imports
from tkinter import filedialog
import pandas as pd
import glob
import os
import streamlit as st

# Functions
def read_folder():
    """
    Reads all the CSVs in a folder

    :return: Pandas dataframe
    """
    # Ask for file path
    folder_path = filedialog.askdirectory()
    print(f"Reading folder: {folder_path}")

    # Making dataframe
    data_df = pd.DataFrame()

    for filename in glob.glob(os.path.join(folder_path, "*.csv")):
        with open(os.path.join(os.getcwd(), filename), 'rb') as f:
            try:
                file_df = pd.read_csv(f, delimiter=",")
            except:
                print("Something went wrong reading the file. Is it a CSV?")

            data_df = pd.concat([data_df, file_df])

    # Sets index to be (0,n)
    files_df = data_df.reset_index()

    return files_df


def read_file(file):
    """
    Reads a CSV file

    :return: Pandas dataframe
    """

    # Read the file to dataframe
    file_df = pd.read_csv(file, delimiter=",")

    # Sets index to be [0,n]
    file_df = file_df.reset_index()

    return file_df


def file_processor(columns=None, target="file", export=False, uploaded=None):
    """
    Reads a CSV file selected by the user with the file browser.

    Column list example: ["frame_no", "timestamp", "rx-green", "ry-green"]

    :param uploaded: file from Streamlit
    :param export: Exports a csv if True
    :param columns: a list of columns desired
    :param target: specify if you want a single file or a folder read: "file" or "folder"
    :return: Pandas dataframe with specified columns
    """

    # Read file or file path
    if target == "file":
        data_df = read_file(uploaded)

    elif target == "folder":
        data_df = read_folder()

    else:
        raise Exception(
            f"Target for file processor defined incorrectly\n\n"
            f"The target must be either 'file' or 'folder'"
        )

    # Selects columns to keep
    if columns is not None:
        data_df = data_df[columns]

    if export:
        data_df.to_csv("Data.csv", index=False)

    return data_df


def na_dropper(df, threshold=None):
    """
    Drops any row with missing data and drops columns that don't hit the threshold

    :param df: any pandas dataframe
    :param threshold: minimum amount of data points for a column if the threshold is 0 then no columns with be dropped
    :return: cleaned pandas dataframe
    """

    if threshold is not None:
        df.dropna(axis=1, thresh=threshold, inplace=True)

    df.dropna(axis=0, how="any", inplace=True)

    return df
