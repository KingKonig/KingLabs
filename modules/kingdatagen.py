import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def express_gen(expression, lower_lim, upper_lim, n, scatter):
    # Setup dataframe
    df = pd.DataFrame(columns=["x", "y"])

    # Find list of x's to use
    x = lower_lim
    x_list = [lower_lim]

    while x <= upper_lim:
        x += (upper_lim - lower_lim) / n

        if x > upper_lim:
            break

        x_list.append(x)

    # Iterate function over x values
    for x in x_list:
        y = eval(expression)

        point_df = pd.DataFrame([[x, y]], columns=["x", "y"])
        df = pd.concat([df, point_df], ignore_index=True)

    # Plot
    plt.style.use("dark_background")
    fig, axs = plt.subplots(1, 1)

    if scatter:
        axs.scatter(
            df["x"],
            df["y"]
        )

    else:
        axs.plot(
            df["x"],
            df["y"]
        )

    axs.set_title("Generated Function")
    axs.set_xlabel("x")
    axs.set_ylabel("y")

    # Output
    return df, fig


if __name__ == "__main__":
    data = express_gen(
        input("Input an expression: "),
        int(input("Lower limit: ")),
        int(input("Upper limit: ")),
        100,
        True
    )

    print(data)
