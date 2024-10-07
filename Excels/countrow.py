import pandas as pd

# Load the Excel file
df = pd.read_excel(r'C:\sus_reports\Py\Simona Fleanta.xlsx', sheet_name='Company_Data')

# Count the number of rows
row_count = df.shape[0]

# Display the DataFrame and the row count
#print(df)
print(f"Number of rows: {row_count}")
