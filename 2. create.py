import pandas as pd

data ={
    "Name": ["Udaya Sri", "Lahari", "Veda Brahmani"],
    "Age": [20, 18, 12],
    "State": ["Punjab", "Rajasthan", "Telangana"]
}

df = pd.DataFrame(data)
print(df)

df.to_csv("Data.csv", index = False)
df.to_excel("Data.xlsx", index = False)
df.to_json("Data.json", index = False)
