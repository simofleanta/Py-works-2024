import psycopg2
from psycopg2 import sql

# Define your connection parameters
conn_params = {
    'dbname': '....',  # Replace with your database name
    'user': '....',  # Replace with your database username
    'password': '......',  # Replace with your database password
    'host': '.....',
    # 'port': 5433  # Uncomment if you need to specify the port
}

try:
    # Establish the connection
    conn = psycopg2.connect(**conn_params)
    print("Connection established successfully.")

    # Create a cursor object
    cursor = conn.cursor()

    # Replace this query with one for a different table you want to see
    cursor.execute("SELECT * FROM your_table_name t LIMIT 10;")  # Replace with your desired table
    rows = cursor.fetchall()

    # Print the retrieved rows
    for row in rows:
        print(row)

except Exception as e:
    print(f"Error connecting to the database: {e}")

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()
        print("Connection closed.")
