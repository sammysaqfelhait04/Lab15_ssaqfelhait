"""
Program Name: Lab 15  Cubic Numbers Plot
Author: Sammy Saqfelhait
Purpose: This program create two plots to show cubic numbers using matplotlib.
It shows first 5 cubes and also first 5000 cubes.
Date: 04/30/2026
"""

import matplotlib.pyplot as plt

x_values_5 = [1, 2, 3, 4, 5]
y_values_5 = [1, 8, 27, 64, 125]

plt.figure()
plt.plot(x_values_5, y_values_5)
plt.title("First 5 Cubes")
plt.xlabel("Value")
plt.ylabel("Cube of Value")

plt.savefig("cubes_5.png")
plt.close()