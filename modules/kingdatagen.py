import pandas as pd
import numpy as np


def express_gen(expression, lower_lim, upper_lim):
    df = pd.DataFrame(columns=["x", "y"])
    for x in range(int(lower_lim), int(upper_lim)):
        y = eval(expression)
        # print(f"({x}, {y})")

        point_df = pd.DataFrame([[x], [y]], columns=["x", "y"])
        df = pd.concat([df, point_df], ignore_index=True)

    return df


if __name__ == "__main__":
    data = express_gen(input("Input an expression: "), input("Lower limit: "), input("Upper limit: "))

    print(data)
