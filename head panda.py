import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Aman", "Riya", "Karan"],
    "Marks": [80, 90, 75, 85, 95]
}

df = pd.DataFrame(data)

print(df.head())