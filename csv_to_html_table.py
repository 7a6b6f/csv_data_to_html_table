import pandas as pd

# read the csv file
a = pd.read_csv("test.csv")

# save as html file
a.to_html("Table.html")

# assign it to a variable (string)
html_file = a.to_html()
