import pandas as pd

data = {
    "Name": ["Tiger", "Lion", "Elephant", "Cheetah", "Fox", "Giraffee", "Bear", "Panther", "Deer", "Rabbit"],
    "Age": [20, 23, 34, 19, 24, 40, 38, 27, 23, 25],
    "Salary": [38000, 45000, 23000, 56000, 34000, 29000, 70000, 46000, 52000, 26000],
    "Experience": [3, 5, 2, 1, 5, 3, 2, 6, 8, 2]
}

df = pd.DataFrame(data)

filtered_or = df[(df["Age"] > 32) | (df["Experience"] < 4)]
print(filtered_or)
