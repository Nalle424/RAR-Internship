from DBConnection import mysqlconnect
import MailService
import mysql.connector
import os
import json

# Instantiate SQL Statementss
# DataLog_query = "INSERT INTO DataLog (Dato, PersonTemp, RoomTemp, Mask, Age, Gender, Emotion, Height, NoFeverID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)" % (values)
SystemLog_query = "INSERT INTO SystemLog (FileDescription) VALUES (%s)"

def insertDataFromTextFileIntoDataLog():
    # Connecting to the database
    conn = mysqlconnect()

    # Getting the file path
    path = "/home/nalle/InsertAndDeleteData"
    dirs = os.listdir(path)

    # Getting the cursor
    cur = conn.cursor()
    conn.autocommit = False

    # Reads through each line in each file from directory that ends with ".log" and inserts their keys and values into the database
    try:
        for i in dirs:
            if i.endswith(".log"):
                with open(path + "/" + i, "r") as f:
                    reader = f.readlines()
                    for row in reader:
                        my_dic = json.loads(row)
                        columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in my_dic.keys())
                        values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in my_dic.values())
                        DataLog_query = "INSERT INTO %s (%s) VALUES (%s)" % ('DataLog', columns, values)

                        values = my_dic.values()
                        values_list = list(values)
                        a_value = values_list[1]

                        if(float(a_value) >= 38):
                            print("Så det sgu mail tid!")
                            # MailService.mailMain()

                        cur.execute(DataLog_query)
                    
                        conn.commit()
                        print("Data was inserted")
                    
        deleteAllFilesFromDirectory()

    except mysql.connector.Error as e:
        print(f"Error. Could not insert data from text file. Rollback happened: {e}")
        conn.rollback()
    
    finally:
        cur.close()
        conn.close()

def insertFilesFromDirIntoSystemLog():
    # Connecting to the database
    conn = mysqlconnect()

    # Getting the file path
    path = "/home/nalle/TESTLOG"
    dirs = os.listdir(path)

    # Getting the cursor
    cur = conn.cursor()
    conn.autocommit = False

    # Iterates through each file in diretory and inserts a reference to them into the database
    try:
        for f in dirs:
            # print (f)
            cur.execute(SystemLog_query, (f,))
        
        conn.commit()
        print("Data was inserted")
    
    except mysql.connector.Error as e:
        print(f"Error. Could not insert files from directory. Rollback happened: {e}")
        conn.rollback()
    
    finally:
        cur.close()
        conn.close()

def deleteAllFilesFromDirectory():
    # Getting the file path
    path = "/home/nalle/InsertAndDeleteData"
    
    # Iterates each file in directory and deletes them if they end with ".log"
    try:
        for f in os.scandir(path):
            if f.name.endswith(".log"):
                os.unlink(f)
        
        print("All Files were deleted")
    
    except:
        print("Couldn't delete all the files")

insertDataFromTextFileIntoDataLog()