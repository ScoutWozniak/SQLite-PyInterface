import sqlite3 as sql
from colorama import Fore, Style
from colorama import init as colorama_init

# DataBase handles most functions you'd need it for.
# TODO: I don't like how this is set up currently.
#Maybe create a seperate class to do things with the database and keep this as functions they'd use.

printDebugMessage = False

class DataBase():
    tables : list
    def __init__(self, dbName : str) -> None:
        self.dbName = dbName
        self.tables = []
        self.getAllTables()
    
    def initDataBase(self) -> None:
        self.conn = sql.connect(self.dbName)
    
    # Returns a bool based on wether it was succesful or not
    def createTable(self, addTable) -> bool:
        self.initDataBase()

        command = f"CREATE TABLE {addTable.name} ("

        for entry in addTable.values:
            command += f"\n {entry} {addTable.values[entry].GetSQLFormat()},"
        command = command[:len(command)-1]
        command += ")"
        
        TryPrint(command)

        # TODO: This feels a bit hacky.  Replace this in general with a function to check if the table exists.
        try:
            self.conn.execute(command)
        except:
            TryPrint("ERROR - Table already exists!!!", True)
            self.conn.close()
            return False
        
        self.conn.commit()
        self.conn.close()
        self.tables.append(addTable)
        return True
    
    def getAllTables(self) -> None:
        self.initDataBase()
        command = """SELECT name FROM sqlite_master
        WHERE type = 'table';"""
        cur = self.conn.cursor()
        self.conn.execute(command)
        rows = cur.fetchall()
        print(rows)


# Refers to an individual table in SQL
# Whenever a table is referenced or created in the database these are automatically created
# TODO: Seperation between the values of data and the values of the 
class Table():
    name : str = ""
    values : dict
    def __init__(self, name, values) -> None:
        self.name = name
        self.values = values


# These classes are automatically handled by the datababse class to print out their correct strings.  Means we do less dirty work
class SQLValue:
    def GetSQLFormat(self) -> str:
        return ""

class VarChar(SQLValue):
    def __init__(self, val : int) -> None:
        self.val = val
    
    def GetSQLFormat(self) -> str:
        return f"varchar({self.val})"

# TODO: Need better distinction from inbuilt int and this
class Int(SQLValue):
    def GetSQLFormat(self) -> str:
        return "Int"



def TryPrint(text : str, error : bool = False) -> None:
    toPrint = text
    if (error):
        toPrint = f"{Fore.RED}" + text +  f"{Style.RESET_ALL}"
    if (printDebugMessage):
        print(toPrint)