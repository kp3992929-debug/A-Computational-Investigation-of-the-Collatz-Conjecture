numbers = [x["number"] for x in data]
steps = [x["steps"] for x in data]

mean_x = sum(numbers) / len(numbers)
mean_y = sum(steps) / len(steps)

numerator = 0
denominator_x = 0
denominator_y = 0

for i in range(len(numbers)):

    x = numbers[i]
    y = steps[i]

    numerator += (x - mean_x) * (y - mean_y)
    denominator_x += (x - mean_x) ** 2
    denominator_y += (y - mean_y) ** 2

correlation = numerator / math.sqrt(
    denominator_x * denominator_y
)

print("Correlation:", correlation)
