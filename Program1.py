import numpy as np
import matplotlib.pyplot as plt

x = [1.35, 2.5, 0.71, .32, 0.78, 0.94, 1.78, 0.71, 1.5, 2.6,
     0.96, 1.7, 1.18, 1, 1.2, 1.6, 2.2, 1.54, 1.66, 2.31,
     1.2, 0.5, 3.3, 1.8, 0.46, 0.7, 1.7, 1.06, 0.34, 1.35]

y = [2, 3, 5, 10, 9, 8, 2, 1, 7, 5,
     9, 2, 4, 6, 2, 3, 10, 9, 3, 5,
     1, 5, 8, 2, 4, 4, 9, 7, 1, 7]

plt.xlabel("Magnitude")
plt.ylabel("Count")
plt.title("Corona California Earth Quake Activity")
x_pos = np.arange(len(x))
plt.bar(x_pos, y, width=1.0, fill=False, align='edge')
plt.xticks(x_pos, x)
plt.margins(0)
plt.tight_layout()
plt.show()