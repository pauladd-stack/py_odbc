from dotenv import load_dotenv
import pyodbc
import os
load_dotenv()



def main():

    # CONNECTION_STRING="DSN=TestODBC;UID=test;PWD=test"
    connection_string = os.getenv("CONNECTION_STRING")

    if connection_string is None:
        raise ValueError("No CONNECTION_STRING found in environment variables")

    try:
        conn = pyodbc.connect(connection_string)
        print("Connection successful")
    except pyodbc.Error as e:
        print("Error: ", e)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM TestTable")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()