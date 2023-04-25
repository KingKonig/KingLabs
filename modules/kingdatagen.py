import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def express_gen(expression, lower_lim, upper_lim, n, scatter, y_label):
    # Setup dataframe
    df = pd.DataFrame(columns=["x", y_label])

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

        point_df = pd.DataFrame([[x, y]], columns=["x", y_label])
        df = pd.concat([df, point_df], ignore_index=True)

    # Plot
    plt.style.use("dark_background")
    fig, axs = plt.subplots(1, 1)

    if scatter:
        axs.scatter(
            df["x"],
            df[y_label]
        )

    else:
        axs.plot(
            df["x"],
            df[y_label]
        )

    axs.set_title("Generated Function")
    axs.set_xlabel("x")
    axs.set_ylabel(y_label)

    # Output
    return df, fig
