import pandas as pd

data = {
    "Name": ["Tiger", "Lion", "Elephant", "Cheetah", "Fox", "Giraffee", "Bear", "Panther", "Deer", "Rabbit"],
    "Age": [20, 23, 34, 19, 24, 40, 38, 27, 23, 25],
    "Salary": [38000, 45000, 23000, 56000, 34000, 29000, 70000, 46000, 52000, 26000],
    "Experience": [3, 5, 2, 1, 5, 3, 2, 6, 8, 2]
}

df = pd.DataFrame(data)
print(df)
print(" ")
df.insert(0, "Employee id", [25001, 25002, 25003, 25004, 25005, 25006, 25007, 25008, 25009, 25010])
print(df)
