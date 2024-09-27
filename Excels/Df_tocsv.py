import pandas as pd

# Load the CSV file
df = pd.read_csv(r'C:\sus_reports\Py\welt.csv')

# Clean the column names by stripping leading/trailing spaces
df.columns = df.columns.str.strip()

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

# Save the modified DataFrame back to a CSV file
df.to_csv(r'C:\sus_reports\Py\welt_modified.csv', index=False)
