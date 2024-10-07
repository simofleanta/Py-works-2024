# took the excel test sheet and set it onto sql 

import pandas as pd
import sqlite3

# Load the Excel file
df = pd.read_excel(r'C:\sus_reports\Py\Simona Fleanta.xlsx', sheet_name='Company_Data')

# Ensure proper UTF-8 handling for string columns (though Excel typically handles encoding well)
df = df.applymap(lambda x: x.encode('utf-8').decode('utf-8') if isinstance(x, str) else x)

# Create (or connect to) an SQLite database
conn = sqlite3.connect(r'C:\sus_reports\Py\welt_data.db')

# Write the DataFrame to the SQLite database
df.to_sql('Simona_Fleanta', conn, if_exists='replace', index=False)

# Close the connection
conn.close()

print("DataFrame has been written to the SQL database successfully.")
