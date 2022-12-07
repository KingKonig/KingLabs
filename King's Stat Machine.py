# Imports
from modules import kingfiles, kingstats
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stat
import numpy as np

# Main
# Prepare Data ---------------------------------------------------------------------------------------------------------
columns = [
    "Time(seconds)",
    "Load Cell (lbf)",
    "Run Tank Pressure (psig)",
    "Combustion Chamber Pressure (psig)",
    "Supply Tank Pressure (psig)"
]
data = kingfiles.file_processor(columns, "files", True)
data = kingfiles.na_dropper(data)


print(
    f"--------------------------------Howdy, thanks for using the King's Stat Machine--------------------------------\n"
    f"---------------------------------------------------Have Fun!---------------------------------------------------\n"
)

# Calcs ----------------------------------------------------------------------------------------------------------------


# Plots ----------------------------------------------------------------------------------------------------------------
# Example Plot
# plt.style.use("dark_background")
# fig, axs = plt.subplots(1, 1)
#
# Time vs X-Position
# axs[0, 0].scatter(
#     data["timestamp"] / 1000,
#     data["position_px_x-green"],
#     s=10,
#     c="green"
# )
#
# axs[0, 0].set_title("Time vs X-Position")
# axs[0, 0].set_xlabel("Time (s)")
# axs[0, 0].set_ylabel("X-Position (pixels)")

# Time vs Y-Position
# axs.plot(
#     data["timestamp"] / 1000,
#     data["position_px_y-green"],
#     # s=10,
#     c="blue"
# )

# plt.show()
# plt.savefig("fig.png")
