# Imports
from modules import kingfiles, kingstats, kingfunky
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stat
import numpy as np
import streamlit as st

# Main
# Prepare Data ---------------------------------------------------------------------------------------------------------
columns = [
    "Time(seconds)",
    "Load Cell (lbf)",
    "Run Tank Pressure (psig)",
    "Combustion Chamber Pressure (psig)",
    "Supply Tank Pressure (psig)"
]

start = 138
end = 142

data = kingfiles.file_processor(columns, "file", False)
data = kingfiles.na_dropper(data)
data = kingfunky.data_cropper(data, start, end)


# print(
#     f"--------------------------------Howdy, thanks for using the King's Stat Machine--------------------------------\n"
#     f"---------------------------------------------------Have Fun!---------------------------------------------------\n"
# )

# Calcs ----------------------------------------------------------------------------------------------------------------


# Plots ----------------------------------------------------------------------------------------------------------------
plt.style.use("dark_background")
fig, axs = plt.subplots(2, 2)
# plt.tight_layout()
plt.subplots_adjust(wspace=0.5, hspace=0.5)

# Time vs Load Cell
axs[0, 0].plot(
    data["Time(seconds)"],
    data["Load Cell (lbf)"],
    c="green"
)

axs[0, 0].set_title("Load Cell")
axs[0, 0].set_xlabel("Time (s)")
axs[0, 0].set_ylabel("(lbf)")

# Time vs Run Tank Pressure
axs[0, 1].plot(
    data["Time(seconds)"],
    data["Run Tank Pressure (psig)"],
    c="green"
)

axs[0, 1].set_title("Run Tank Pressure")
axs[0, 1].set_xlabel("Time (s)")
axs[0, 1].set_ylabel("RT Pressure (psig)")

# Time vs Supply Tank Pressure
axs[1, 1].plot(
    data["Time(seconds)"],
    data["Supply Tank Pressure (psig)"],
    c="green"
)

axs[1, 1].set_title("Supply Tank Pressure")
axs[1, 1].set_xlabel("Time (s)")
axs[1, 1].set_ylabel("ST Pressure (psig)")

# Time vs Chamber Pressure
axs[1, 0].plot(
    data["Time(seconds)"],
    data["Combustion Chamber Pressure (psig)"],
    c="green"
)

axs[1, 0].set_title("Chamber Pressure")
axs[1, 0].set_xlabel("Time (s)")
axs[1, 0].set_ylabel("Chamber Pressure (psig)")

# plt.show()
# plt.savefig("fig.png")

# Web GUI

st.title("SET Data")

st.pyplot(fig)
