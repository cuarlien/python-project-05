import pandas as pd
data = {
    "Name": ["Rahul", "Priya", "Aman", "Simran"],
    "Age": [20, None, 21, None],
    "Marks": [85, 90, None, 75]
}
df = pd.DataFrame(data)
print(df)
