from DBConnection import mysqlconnect
import mysql.connector

# Instantiate SQL Statements
query = "INSERT INTO SystemLog (FileDescription) VALUES (%s)"

def insertTextFile():
    # Connecting to the database
    conn = mysqlconnect()

    # Getting the cursor
    cur = conn.cursor()
    conn.autocommit = False

    # Get file path
    file = open('TESTLOG.txt', 'rb')
    file_content = file.read()
    file.close()

    # Insert file into the database
    try:
        cur.execute(query, (file_content,))
        conn.commit()
        print("Data was inserted")

    except mysql.connector.Error as e:
        print(f"Error. Could not insert data. Rollback happened: {e}")
        conn.rollback()
    
    conn.close()