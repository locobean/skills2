# writing
import csv

rows = []

header = ['State', 'Population', 'Capital']
data = [['Vic', 664915, 'Melbourne'], ['NSW', 8189266, 'Sidney'], ['SA', 1773243, 'Adelaide'
], ['WA',2681633, 'Perth'], ['Tasmania',541479], ['Queensland',5221170, 'Brisbane'], ['ACT',432266, 'Canberra'], ['NT',246338, "Darwin"]
]
with open('states.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    csvwriter.writerows(data)

