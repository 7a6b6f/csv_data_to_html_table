
import csv

with open('data.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    table_data = []
    for row in csvreader:
        table_data.append(row)

html = "<table>"
for row in table_data:
    html += "<tr>"
    for cell in row:
        html += "<td>" + cell + "</td>"
    html += "</tr>"
html += "</table>"

print(html)
