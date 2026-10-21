import pandas as pd

df = pd.DataFrame({
    "Student": ["Aman", "Riya", "Karan", "Neha", "Rohit", "Simran"],
    "Marks": [78, 85, 92, 67, 88, 95]
})

print(df.tail(4))