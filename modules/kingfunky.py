# Imports

# Functions
def data_filter(data, start, end):
    rows_to_delete = list()
    for i in range(len(data)):
        if data.iloc[i, 1] < start:
            rows_to_delete.append(i)

        if data.iloc[i, 1] > end:
            rows_to_delete.append(i)

    data = data.drop(data.index[rows_to_delete], index=None)

    # data.to_csv("Filtered Data.csv", index=False)

    return data
