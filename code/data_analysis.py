import csv
import statistics
import math

data = []

with open("collatz_data.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        number = int(row["Starting Number"])
        steps = int(row["Steps"])
        maximum = int(row["Maximum Value"])

        ratio = maximum / number

        data.append({
            "number": number,
            "steps": steps,
            "maximum": maximum,
            "ratio": ratio
        })

steps = [x["steps"] for x in data]
maximums = [x["maximum"] for x in data]
ratios = [x["ratio"] for x in data]

print("Mean stopping time:", statistics.mean(steps))
print("Median stopping time:", statistics.median(steps))

print("Mean maximum value:", statistics.mean(maximums))
print("Median maximum value:", statistics.median(maximums))

print("Mean maximum/starting ratio:", statistics.mean(ratios))
print("Median maximum/starting ratio:", statistics.median(ratios))
