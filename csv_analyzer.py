import csv

filename = input("Enter CSV file name: ")

try:
    with open(filename, "r") as file:
        data = list(csv.DictReader(file))

    print("\nTotal Records:", len(data))

    if data:
        print("Columns:", list(data[0].keys()))

        for column in data[0].keys():
            print("\nColumn:", column)

            values = [row[column] for row in data]

            print("Sample values:", values[:5])

except FileNotFoundError:
    print("File not found.")
