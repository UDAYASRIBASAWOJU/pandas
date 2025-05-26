data = {
    "Name": ["Tiger", "Lion", "Elephant", "Cheetah", None, "Giraffee", "Bear", "Panther", "Deer", "Rabbit"],
    "Age": [20, 23, 34, 19, 24, None, 38, 27, 23, None],
    "Salary": [38000, None, 23000, 56000, 34000, 29000, 70000, 46000, 52000, 26000],
    "Experience": [3, 5, 2, 1, 5, 3, 2, 6, None, 2]
}

df = pd.DataFrame(data)
print(df)
print("")
df.dropna(inplace = True)
print(df)
print("")
df.dropna(axis= 0, inplace = True)
print(df)
