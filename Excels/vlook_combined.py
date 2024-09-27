import pandas as pd

# Assuming the data is in a CSV or directly creating the DataFrame
data = {
    "Name": ["Joseph Price", "Olivia Wilson", "Christopher Reed", "Ashley Schroeder", "kerry Allen", 
             "Renata Hall", "Michael Harris", "Andre Lawson", "Anthony Ivanov", "Dalia Pelayo", 
             "Diana Gabriene", "Sayeed Yasseen", "Elis Turner", "Malik Barden"],
    "Addresse1": ["Str Andrei Saguna", "Str Lunga", "Str Scurta", "Str de mijloc", "Str Alba", 
                  "Str Venus", "Str Lunii", "Str Marte", "Str Caragiale", "Str Babes", 
                  "Str Ioncsy", "Str Ivanov", "Str Muzeui", "Str Neagra"],
    "Addresse2": ["Sibiu", "Brasov", "Alba", "Brasov", "Deva", "Cluj", 
                  "Brasov", "Timisoara", "Timisoara", "Sibiu", 
                  "Medias", "Deva", "Cluj", "Cluj"],
    "Phonenumber": ["7643000009", "7553371352", "7334567800", "7837422222", "7239807600", 
                    "7492323546", "3987456392", "7492387465", "2846192372", "2402719283", 
                    "7892735294", "7659273472", "1836404038", "1936287300"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Perform the lookup for 'Anthony Ivanov'
name_to_lookup = "Anthony Ivanov"
result = df.loc[df['Name'] == name_to_lookup, ['Addresse1', 'Phonenumber']]

# If you want to combine the results into one string
if not result.empty:
    address = result['Addresse1'].values[0]
    phone = result['Phonenumber'].values[0]
    combined = f"{address} | {phone}"
    print(combined)
else:
    print(f"{name_to_lookup} not found.")




///////////////////////////////////////

# or from the excel file

import pandas as pd
import openpyxl  # Required for working with Excel files

# Load the Excel file into a DataFrame
file_path = r'C:\sus_reports\Py\Vlook ex.xlsx'  # Use raw string (r'...') for file path
data = pd.read_excel(file_path)

# Clean the column names by stripping leading/trailing spaces
data.columns = data.columns.str.strip()

# Check the data and the columns
print(data.columns)
print(data)

# Perform the lookup for 'Anthony Ivanov'
name_to_lookup = "Anthony Ivanov"
result = data.loc[data['Name'] == name_to_lookup, ['Addresse1', 'Phonenumber']]

# If you want to combine the results into one string
if not result.empty:
    address = result['Addresse1'].values[0]
    phone = result['Phonenumber'].values[0]
    combined = f"{address} | {phone}"
    print(combined)
else:
    print(f"{name_to_lookup} not found.")
