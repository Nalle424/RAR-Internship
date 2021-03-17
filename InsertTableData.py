from DBConnection import mysqlconnect
import mysql.connector

# Instantiate SQL Statements
insert_data_NoFeverDevice = """
INSERT INTO NoFeverDevice (NoFeverName)
VALUES
    ('NoFever_0001'),
    ('NoFever_0002'),
    ('NoFever_0003'),
    ('NoFever_0004');
"""

insert_data_Adminstration = """
INSERT INTO Adminstration (CompanyName, CompanyAddress, Price, ContactName, ContactPhNo, PurchaseType, Email, NoFeverID) 
VALUES 
    ('TestCompany', 'TestStreet 1', 10000, 'John Doe', 88888888, 'Credit Card', 'testmail@hotmail.com', 1),
    ('TestCompany2', 'TestStreet 2', 10000, 'John Doe', 88888887, 'Credit Card', 'testmail2@hotmail.com', 2),
    ('TestCompany3', 'TestStreet 3', 10000, 'John Doe', 88888886, 'Credit Card', 'testmail3@hotmail.com', 3),
    ('TestCompany4', 'TestStreet 4', 10000, 'John Doe', 88888885, 'Credit Card', 'testmail4@hotmail.com', 4);
"""

insert_data_DataLog = """
INSERT INTO DataLog (Dato, PersonTemp, RoomTemp, Mask, Age, Gender, Emotion, HeightMetric, HeightImperial, NoFeverID)
VALUES
    ('2021-02-01 08:00:00.000', 36.72, 24.45, 'Wrong', 25, 'F', 'Frustrated', 1.54, NULL, 1),
    ('2021-02-02 08:00:00.000', 37.73, 24.60, 'Off', 25, 'F', 'Happy', 1.78, NULL, 1),
    ('2021-02-03 08:00:00.000', 38.47, 16.42, 'On', 25, 'M', 'Sad', 1.63, NULL, 1),
    ('2021-02-04 08:00:00.000', 37.11, 18.71, 'Off', 25, 'M', 'Happy', 1.62, NULL, 1),
    ('2021-02-05 08:00:00.000', 36.56, 19.45, 'On', 25, 'M', 'Sad', 1.64, NULL, 1),

    ('2021-02-01 08:30:00.000', 37.82, 16.06, 'Off', 25, 'M', 'Happy', 1.60, NULL, 2),
    ('2021-02-01 08:30:00.000', 38.37, 21.30, 'On', 25, 'F', 'Sad', 1.78, NULL, 2),
    ('2021-02-01 08:30:00.000', 37.21, 24.21, 'On', 25, 'F', 'Sad', 1.58, NULL, 2),
    ('2021-02-01 08:30:00.000', 34.75, 23.05, 'On', 25, 'M', 'Tired', 1.63, NULL, 2),
    ('2021-02-01 08:30:00.000', 34.30, 24.64, 'On', 25, 'M', 'Happy', 1.52, NULL, 2),

    ('2021-02-01 09:00:00.000', 37.64, 24.12, 'On', 25, 'F', 'Sad', 1.53, NULL, 3),
    ('2021-02-01 09:00:00.000', 38.85, 16.74, 'Off', 25, 'F', 'Sad', 1.47, NULL, 3),
    ('2021-02-01 09:00:00.000', 37.08, 25.42, 'Wrong', 25, 'F', 'Sad', 1.79, NULL, 3),
    ('2021-02-01 09:00:00.000', 34.16, 23.05, 'Off', 25, 'F', 'Frustrated', 1.49, NULL, 3),
    ('2021-02-01 09:00:00.000', 35.17, 21.19, 'On', 25, 'M', 'Happy', 1.90, NULL, 3),

    ('2021-02-01 09:30:00.000', 35.36, 17.33, 'Off', 25, 'F', 'Happy', 1.63, NULL, 4),
    ('2021-02-01 09:30:00.000', 36.72, 19.20, 'On', 25, 'M', 'Frustrated', 1.54, NULL, 4),
    ('2021-02-01 09:30:00.000', 38.49, 16.18, 'Wrong', 25, 'M', 'Happy', 1.76, NULL, 4),
    ('2021-02-01 09:30:00.000', 35.19, 18.13, 'Wrong', 25, 'F', 'Happy', 1.76, NULL, 4),
    ('2021-02-01 09:30:00.000', 34.17, 24.45, 'Wrong', 25, 'M', 'Tired', 1.78, NULL, 4);
"""

def insertTableData():
    # Connecting to the database
    conn = mysqlconnect()

    # Getting the cursor
    cur = conn.cursor()
    conn.autocommit = False


    # Insert Data
    try:
        cur.execute(insert_data_NoFeverDevice),
        cur.execute(insert_data_Adminstration),
        cur.execute(insert_data_DataLog)
    except mysql.connector.Error as e:
        print(f"Error. Insert data is rollbacking: {e}")
        conn.rollback()

    conn.commit()
    print("Inserted all the above data")

    conn.close()

    return cur.fetchall