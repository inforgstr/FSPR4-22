import matplotlib.pyplot as plt
import numpy as np


xpoints = np.array([0, 30, 10])
ypoints = np.array([0, 100, 500])
plt.bar(xpoints, ypoints)
plt.title("Data")
plt.plot(xpoints, ypoints, "+")


xpoints = np.array([0, 20, 30, 40])
ypoints = np.array([0, 200, 300, 1000])
plt.title("Data-2")
plt.plot(xpoints, ypoints)
plt.show()
