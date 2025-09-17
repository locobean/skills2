import csv

rows = []

with open('states.csv', 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)

# Add new header "Capital"
    header.append("Capital")


print(header)
print(rows)