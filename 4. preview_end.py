import pandas as pd

data = pd.read_csv("Overview.csv")
print("Ending rows of data(default 5)")
print(data.tail())
print("")
print("Ending 12 rows of data")
print(data.tail(12))
