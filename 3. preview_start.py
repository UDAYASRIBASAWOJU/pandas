import pandas as pd

data = pd.read_csv("Overview.csv")
print("Starting rows of data(default 5)")
print(data.head())
print("")
print("Starting 12 rows of data")
print(data.head(12))
