import pandas as pd

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
    'Healthy life expectancy at birth':'BirthLife_Expectancy'
}, inplace=True)

# Display the first 30 rows of the updated DataFrame
#print(df.head(30))

# Save the modified DataFrame back to the same CSV file
df.to_csv(r'C:\sus_reports\Py\welt.csv', index=False)
print(df.columns)

# things to automate in python 
#take the document
#clean it
#rename colls
#put it on sqlite3 for queries

#vlook combined
#vlook 
# if ifs
#sumifs
#count 
#merge sells
#replace 
#reseize colls

# VLOOKUP equivalent for Life_Ladder for Denmark
denmark_life_ladder = df.loc[df['Country'] == 'Denmark', 'Life_Ladder'].values

if len(denmark_life_ladder) > 0:
    print(f"Life Ladder for Denmark: {denmark_life_ladder[0]}")
else:
    print("Denmark not found in the DataFrame.")
