# Imports

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
