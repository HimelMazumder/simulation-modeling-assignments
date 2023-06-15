import csv
import numpy as np
import matplotlib.pyplot as plt

file = open("SalesData.csv", 'r')
reader = csv.reader(file)
# skips the header row read from csv file
next(reader)

x = []
y = []

a = []
b = []
c = []

for row in reader:
    x.append(int(row[1]))
    a.append(int(row[2]))
    b.append(int(row[3]))
    c.append(int(row[4]))

y.append(a)
y.append(b)
y.append(c)

x_point = np.array(x)
y_point = np.array(y)


for i in range(len(y_point)):
    # line plot
    plt.subplot(2, 1, 1)
    plt.plot(x_point, y_point[i])
    plt.title("Line Plot", loc='left')
    plt.xlabel("Days")
    plt.ylabel("Products")

    # scatter plot
    plt.subplot(2, 1, 2)
    plt.scatter(x_point, y_point[i])
    plt.title("Scatter Plot", loc='left')
    plt.xlabel("Days")
    plt.ylabel("Products")

plt.subplots_adjust(hspace=0.5)

plt.show()

file.close()
