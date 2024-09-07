import csv
import numpy as np

ARRAY_LEN = 1000

# x is an array of random numbers between 0 and 100
x = np.random.rand(ARRAY_LEN) * 100

# y is an array of random numbers linearly related to x
y_intercept = 13
slope = 1.6
std_dev = 17
residuals = np.random.normal(size=ARRAY_LEN)
y = x * slope + y_intercept + residuals * std_dev

# Write all to file
with open('approxlinear.csv', 'w', newline='') as file:
    csvwriter = csv.writer(file)
    for (xi, yi) in zip(x, y):
        csvwriter.writerow([xi, yi])