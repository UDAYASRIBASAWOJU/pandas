import pandas as pd

data = pd.read_csv("Overview.csv")
print("Displaying info of data")
print(data.info())
