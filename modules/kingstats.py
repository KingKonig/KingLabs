# Imports
import numpy as np
import pandas as pd


# Functions
def interpolate(data_list):
    """
    Linearly Interpolates by finding the value in between every point

    :param data_list: list or 1D array of values
    :return: interpolated list of values
    """

    interpolated_data_list = list()

    for i in range(len(data_list) - 1):
        interpolated_data_list.append(data_list[i])
        interpolated_data_list.append((data_list[i + 1] + data_list[i]) / 2)

    return interpolated_data_list


def extrapolate(slope, intercept, start_x, end_x):
    """
    Linearly extrapolates

    :param slope: slope of line to extrapolate
    :param intercept: y-intercept of line to extrapolate
    :param start_x: x-value to start at
    :param end_x: x-value to end at
    :return: x-points list, y-points list
    """

    # Extrapolate first and last points of line
    start_y = (slope * (start_x - intercept[0])) + intercept[1]
    end_y = (slope * (end_x - intercept[0])) + intercept[1]

    x_points = [start_x, end_x]
    y_points = [start_y, end_y]

    return x_points, y_points


def f_finite_d(list_a, list_b):
    """
    Performs a forward finite difference given two sets of data. Change in A over change in B.

    :param list_a: List of A values
    :param list_b: list of B values
    :return: List of rates E.G. dA/dB
    """

    delta_a = list()

    for i in range(len(list_a) - 1):
        delta_a_k = (list_a[i + 1] - list_a[i]) / (list_b[i + 1] - list_b[i])
        delta_a.append(delta_a_k)

    return delta_a


def b_finite_d(list_a, list_b):
    """
    Performs a backward finite difference given two sets of data. Change in A over change in B.

    :param list_a: List of A values
    :param list_b: list of B values
    :return: List of rates E.G. dA/dB
    """

    delta_a = list()

    for k in range(len(list_a) - 1):
        delta_a_k = (list_a[k - 1] - list_a[k]) / (list_b[k - 1] - list_b[k])
        delta_a.append(delta_a_k)

    return delta_a


def c_finite_d(list_a, list_b):
    """
    Performs a central finite difference given two lists((change in A) / (change in B))

    :param list_a: A LIST
    :param list_b: B LIST
    :return: dA/dB LIST
    """

    da_db = list()

    for k in range(1, len(list_a) - 1):
        da_db_k = (list_a[k + 1] - list_a[k - 1]) / (list_b[k + 1] - list_b[k - 1])
        da_db.append(da_db_k)

    return da_db


# def c_finite_d(df_a, df_b):
#     """
#     Performs a central finite difference given two lists((change in A) / (change in B))
#
#     :param df_a: 1D pd DataFrame A
#     :param df_b: 1D pd DataFrame B
#     :return: dA/dB 1D pd DataFrame
#     """
#
#     da_db = pd.DataFrame()
#
#     for k in range(1, len(df_a) - 1):
#         da_db_k = (df_a[k + 1] - df_a[k - 1]) / (df_b[k + 1] - df_b[k - 1])
#         da_db.append(da_db_k)
#
#     return da_db


def moving_average(data_list, n=3):
    """
    Performs a moving average over n points

    :param data_list: data in list type
    :param n: amount of points to average over
    :return: list of averaged points
    """

    averaged_data = list()

    for i in range(len(data_list) - n):
        j_sum = 0

        for j in range(n):
            j_sum += data_list[i + (j + 1)]

        average_i = j_sum / n
        averaged_data.append(average_i)

    return averaged_data


def distance(x1, x2, y1, y2):
    """
    Gives the distance between two points given their x and y coordinates

    :param x1: x value of 1st point
    :param x2: x value of 2nd point
    :param y1: y value of 1st point
    :param y2: y value of 2nd point
    :return: distance value magnitude
    """

    dist = np.sqrt(np.power(x2 - x1, 2) + np.power(y2 - y1, 2))

    return dist


def magnitude(x_list):
    """
    Calculates the magnitude or pythagorean theorem of a list of values

    (a^2, b^2, c^2, ...)^(1/2)

    :param x_list:
    :return:
    """

    square_xs = 0

    for x in x_list:
        square_xs += np.power(x, 2)

    magnitude_out = np.sqrt(square_xs)

    return magnitude_out
