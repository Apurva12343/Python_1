import pyodbc

# Connection details
server = 'localhost'  # Replace with your server name or IP address
database = 'AdventureWorks2019'  # Your database name

# Connection string for Windows Authentication
connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"

try:
    # Establish the connection
    conn = pyodbc.connect(connection_string)
    print(f"Connected to the database '{database}' successfully!")

    # Create a cursor and execute a query excluding unsupported columns
    cursor = conn.cursor()
    query = """
    SELECT BusinessEntityID, NationalIDNumber, LoginID, JobTitle
    FROM HumanResources.Employee
    """
    cursor.execute(query)

    # Print the results
    print("Data from the table:")
    for row in cursor.fetchall():
        print(row)

except pyodbc.Error as e:
    print("Error:", e)

finally:
    # Close the connection
    if 'conn' in locals() and conn:
        conn.close()
        print("Connection closed.")
