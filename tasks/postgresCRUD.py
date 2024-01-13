import psycopg2
from psycopg2 import sql

# Database credentials
dbName = 'task1db'
user = 'postgres'
password = 'admin'
host = 'localhost'
port = 5432

# Function to establish a connection to the database
def connect():
    connection = psycopg2.connect(dbname=dbName, user=user, password=password, host=host, port=port)
    return connection, connection.cursor()

# Function to create the table (if not exists)
def createTable(cursor):
    createTableQuery = '''
        CREATE TABLE IF NOT EXISTS sample_data (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            age INT
        )
    '''
    cursor.execute(createTableQuery)

# Function to insert data into the table
def insertData(cursor, name, age):
    insertQuery = sql.SQL('INSERT INTO sample_data (name, age) VALUES ({}, {})').format(
        sql.Literal(name),
        sql.Literal(age)
    )
    cursor.execute(insertQuery)

# Function to read data from the table
def readData(cursor):
    selectQuery = 'SELECT * FROM sample_data'
    cursor.execute(selectQuery)
    rows = cursor.fetchall()
    print("Data in the table:")
    for row in rows:
        print(row)

# Function to update data in the table
def updateData(cursor, name, newAge):
    updateQuery = 'UPDATE sample_data SET age = %s WHERE name = %s'
    cursor.execute(updateQuery, (newAge, name))

# Function to delete data from the table
def deleteData(cursor, name):
    deleteQuery = 'DELETE FROM sample_data WHERE name = %s'
    cursor.execute(deleteQuery, (name,))

# Function to close the cursor and connection
def closeConnection(connection, cursor):
    cursor.close()
    connection.close()

# Main program
try:
    connection, cursor = connect()

    # Create the table
    createTable(cursor)

    # Insert data into the table
    insertData(cursor, 'Ravi Kumar', 28)
    insertData(cursor, 'Priya Singh', 22)
    insertData(cursor, 'Amit Patel', 35)
    insertData(cursor, 'Deepika Sharma', 30)
    insertData(cursor, 'Rahul Verma', 25)
    insertData(cursor, 'Abhishek Tyagi', 24)
    insertData(cursor, 'Yash Arora', 23)
    insertData(cursor, 'Virat Kohli', 36)

    # Read and display data from the table
    readData(cursor)

    # Update data in the table
    updateData(cursor, 'Priya Singh', 23)

    # Read and display updated data from the table
    readData(cursor)

    # Delete data from the table
    deleteData(cursor, 'Amit Patel')

    # Read and display data after deletion
    readData(cursor)

finally:
    # Close the cursor and connection
    closeConnection(connection, cursor)
