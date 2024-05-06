import csv
from matplotlib import pyplot as plt
file = open(r"C:\Users\Ahmed\Desktop\DSP\Project\Subject1_Signals.csv")
csvreader = csv.reader(file)
rows = []
channel1car = []
channel2car = []
channel3car = []
channel1 = []
channel2 = []
channel3 = []
for row in csvreader:
    values = []
    for i in range(len(row)):
        if i == 0:
            channel1.append(float(row[i]))
        if i == 1:
            channel2.append(float(row[i]))
        if i == 2:
            channel3.append(float(row[i]))
        values.append(float(row[i]))
    car = sum(values) / len(values)
    for y in range(len(values)):
        values[y] = values[y] - car
        if y == 0:
            channel1car.append(values[y])
        if y == 1:
            channel2car.append(values[y])
        if y == 2:
            channel3car.append(values[y])
    rows.append(values)
plt.plot(channel1car, channel2car, channel3car)
plt.show()
plt.plot(channel1, channel2, channel3)
plt.show()
