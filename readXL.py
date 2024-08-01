import pandas as pd

# Replace 'input.xlsx' with your Excel file name
file_path = 'Input.xlsx'

# Read the Excel file
df = pd.read_excel(file_path)

# Assuming the first two columns are 'name' and 'arr'
df_filtered = df[df['arr'] > 100000]

# Output the filtered rows
print(df_filtered)

