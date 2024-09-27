import pandas as pd
import sqlite3

#Take the doc
#Clean it
# put it in an sqlt3 db to sql queries 
#Data is real :) WB


# Load the CSV file
df = pd.read_csv(r'C:\sus_reports\Py\welt.csv')

# Clean the column names by stripping leading/trailing spaces
df.columns = df.columns.str.strip()

# Replace NaN values with 0.00
df.fillna(0.00, inplace=True)

# Rename the specified columns
df.rename(columns={
    'Country name': 'Country',
    'Life Ladder': 'Life_Ladder',
    'Log GDP per capita': 'GDP',
    'Social support': 'Social_support',
    'Freedom to make life choices': 'Freedom_choices',
    'Perceptions of corruption': 'Perception_corruption',
    'Positive affect': 'Positive_affect',
    'Negative affect': 'Negative_affect',
    'Healthy life expectancy at birth': 'BirthLife_Expectancy'
}, inplace=True)

# Create a SQLite database (or connect to one)
conn = sqlite3.connect(r'C:\sus_reports\Py\welt_data.db')

# Write the DataFrame to the SQLite database
df.to_sql('welt', conn, if_exists='replace', index=False)

# Close the connection
conn.close()

print("DataFrame has been written to SQL file successfully.")
