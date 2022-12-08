# Imports

# Functions
def data_cropper(data, start, end, export=False):
    rows_to_delete = list()

    for i in range(len(data)):
        if data.iloc[i, 0] < start:
            rows_to_delete.append(i)

        if data.iloc[i, 0] > end:
            rows_to_delete.append(i)

    data = data.drop(data.index[rows_to_delete], index=None)

    if export:
        data.to_csv("Cropped Data.csv", index=False)

    return data
