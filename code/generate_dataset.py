import csv

with open("collatz_data.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Starting Number",
        "Steps",
        "Maximum Value"
    ])

    for a in range(1, 10001):

        c = a
        d = 0
        Max = a

        while c != 1:

            if c % 2 == 0:
                c = c // 2
            else:
                c = 3 * c + 1

            d = d + 1

            if c > Max:
                Max = c

        writer.writerow([a, d, Max])

print("Dataset generated successfully!")
