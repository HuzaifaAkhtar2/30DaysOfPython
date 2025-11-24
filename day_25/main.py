import pandas as pd

# Read the hacker_news.csv file from data directory
csv = pd.read_csv("./data/hacker_news.csv")

# Get the first five rows
print(csv.head())

# Get the last five rows
print(csv.tail())

# Get the title column as pandas series
titles = csv["title"]
print(titles)

# Count the number of rows and columns
csv_shape = csv.shape
print("Number of rows: {}\nNumber of columns: {}".format(csv_shape[0], csv_shape[1]))

# Filter the titles which contain python
python_titles = csv[titles.apply(lambda x: "python" in str(x).lower())]
print(python_titles)

# Filter the titles which contain JavaScript
js_titles = csv[titles.apply(lambda x: "javascript" in str(x).lower())]
print(js_titles)

# Explore the data and make sense of it
print(csv.describe())