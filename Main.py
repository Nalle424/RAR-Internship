from DBConnection import mysqlconnect
from InsertTables import insertTables
from InsertTableData import insertTableData
from InsertEntireTextFile import insertTextFile
from InsertDataIntoDB import insertDataFromTextFileIntoDataLog, insertFilesFromDirIntoSystemLog
from MailService import mailMain
import mysql.connector

def main():
    # insertTables()
    # insertTableData()
    # insertFilesFromDirIntoSystemLog()
    # insertDataFromTextFileIntoDataLog()
    mailMain()


if __name__ == '__main__':
    main()