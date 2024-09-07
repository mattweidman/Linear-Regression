import csv
import math
import matplotlib.pyplot as plt
import numpy as np

# Read data from file
x_arr = []
y_arr = []
with open('approxlinear.csv', newline='') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        x_arr.append(float(row[0]))
        y_arr.append(float(row[1]))

# Convert to numpy
x = np.array(x_arr)
y = np.array(y_arr)
n = len(x_arr)

# Compute y-intercept and slope.
# Derivation: https://spia.uga.edu/faculty_pages/mlynch/teaching/ols/OLSDerivation.pdf
x_sum = x.sum()
y_sum = y.sum()
slope = ((x * y).sum() - x_sum * y_sum / n) / ((x * x).sum() - x_sum * x_sum / n)
y_intercept = (y_sum - slope * x_sum) / n
print("slope:", slope)
print("y-intercept:", y_intercept)

# Compute variance and standard deviation
y_predicted = x * slope + y_intercept
variance = np.average((y - y_predicted)**2)
print("variance:", variance)
print("standard deviation:", math.sqrt(variance))

# Plot params
min_x = 0
max_x = 100
min_y = 0
max_y = 225

# Plot data points
plt.plot(x, y, marker='o', markersize=2, linestyle='', color='red')

# Plot the best fit line
plt.plot([min_x, max_x], [y_intercept, y_intercept + slope * max_x])

# Scale to the desired size
plt.axis((min_x, max_x, min_y, max_y))

plt.show()