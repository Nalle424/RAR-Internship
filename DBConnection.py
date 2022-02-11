# Import Modules
import mysql.connector
from mysql.connector import errorcode


def mysqlconnect():
    try:
        db_connection = mysql.connector.connect(
            user="Nalle",
            password="************",
            host="localhost",
            port="3306",
            database="testDatabase"
        )
    
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL Platform: {e}")
        # if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        #     print("Authetication Error")
        # else:
        #     print("Database does not exist")
    
    return db_connection
