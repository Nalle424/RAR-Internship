from DBConnection import mysqlconnect
import mysql.connector

# Instantiate SQL Statements
create_table_NoFeverDevice = "CREATE TABLE IF NOT EXISTS NoFeverDevice(NoFeverID INT(4) UNSIGNED AUTO_INCREMENT, NoFeverName VARCHAR(30), PRIMARY KEY (NoFeverID));"
create_table_Adminstration = """
CREATE TABLE IF NOT EXISTS Adminstration(
CompanyName     VARCHAR(30) NOT NULL,
CompanyAddress  VARCHAR(30) NOT NULL,
Price           DECIMAL(10,2) NOT NULL,
ContactName     VARCHAR(30) NOT NULL,
ContactPhNo     INT(8) UNSIGNED NOT NULL,
PurchaseType    VARCHAR(20) NOT NULL,
Email           VARCHAR(50) NOT NULL,
NoFeverID       INT(4) UNSIGNED,
PRIMARY KEY (ContactPhNo),
CONSTRAINT fk_AdminNoFeverID FOREIGN KEY (NoFeverID) REFERENCES NoFeverDevice(NoFeverID)
ON DELETE CASCADE
ON UPDATE CASCADE
);
"""
create_table_DataLog = """
CREATE TABLE IF NOT EXISTS DataLog (
FaceID          INT(8) UNSIGNED AUTO_INCREMENT,
Dato            DATETIME NOT NULL,
PersonTemp      DECIMAL(3,1) UNSIGNED NOT NULL,
RoomTemp        DECIMAL(4,2) UNSIGNED NOT NULL,
 Mask            ENUM('On', 'Off', 'Wrong') DEFAULT 'Off',
Age             int(3) UNSIGNED NOT NULL,
Gender          ENUM('M', 'F'),
Emotion         ENUM('Happy', 'Sad', 'Frustrated', 'Tired'),
HeightMetric    DECIMAL(3,1) UNSIGNED NOT NULL,
HeightImperial  DECIMAL(2,1) UNSIGNED,
NoFeverID       INT(4) UNSIGNED,
PRIMARY KEY (FaceID),
CONSTRAINT fk_DataLogNoFeverID FOREIGN KEY (NoFeverID)
REFERENCES NoFeverDevice(NoFeverID)
ON DELETE CASCADE
ON UPDATE CASCADE
);
"""
create_table_SystemLog = """
CREATE TABLE IF NOT EXISTS SystemLog (
ID              INT(8) UNSIGNED AUTO_INCREMENT,
Dato            DATETIME NOT NULL,
LogType         VARCHAR(50),
NoFeverID       INT(4) UNSIGNED,
PRIMARY KEY (ID),
CONSTRAINT fk_SystemLogNoFeverID FOREIGN KEY (NoFeverID)
REFERENCES NoFeverDevice(NoFeverID)
ON DELETE CASCADE
ON UPDATE CASCADE
);
"""


def insertTables():
    # Connecting to the database
    conn = mysqlconnect()

    # Getting the cursor
    cur = conn.cursor()
    conn.autocommit = False

    # Insert tables
    try:
        cur.execute(create_table_NoFeverDevice),
        cur.execute(create_table_Adminstration),
        cur.execute(create_table_DataLog),
        cur.execute(create_table_SystemLog)
        
        conn.commit()
        print("Inserted all the above tables")

    except mysql.connector.Error as e:
        print(f"Error. Insert table is rollbacking: {e}")
        # if e.errno == errorcode.ER_TABLE_EXISTS_ERROR:
        #     print("Tables are already created")
        # else:
        #     print("Something went wrong when creating tables")
        conn.rollback()
        
    finally:
        cur.close()
        conn.close()