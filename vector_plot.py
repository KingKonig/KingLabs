# Modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load file
file_path_x = "C:/Users/jason/PycharmProjects/KingLabs/data/x1.csv"
file_path_y = "C:/Users/jason/PycharmProjects/KingLabs/data/y1.csv"

# Plot
vectors_x = pd.read_csv(file_path_x)
vectors_y = pd.read_csv(file_path_y)

x_size = vectors_x.shape[1]
y_size = vectors_x.shape[0]

x = np.arange(0, x_size)
y = np.arange(0, y_size)
X, Y = np.meshgrid(x, y)

plt.quiver(X, Y, vectors_x.values, vectors_y.values, scale=50000)

plt.xlabel('X step')
plt.ylabel('Y step')
plt.title('Sharp Point and Bar Field')
plt.show()
