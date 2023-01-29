import pandas as pd

# Define the data to be stored
data = {"Name": ["John", "Jane", "Jim"],
        "Age": [30, 32, 28],
        "Country": ["USA", "Canada", "UK"]}

# Create a pandas DataFrame with the data
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel("data.xlsx", index=False)
