import sqlite3 as sql

# DataBase handles most functions you'd need it for.
# TODO: I don't like how this is set up currently.
#Maybe create a seperate class to do things with the database and keep this as functions they'd use.

class DataBase():
    tables : list
    def __init__(self, dbName : str) -> None:
        self.dbName = dbName
        self.tables = []
        self.getAllTables()
    
    def initDataBase(self):
        self.conn = sql.connect(self.dbName)
    
    def createTable(self, addTable):
        self.initDataBase()

        command = f"CREATE TABLE {addTable.name} ("

        for entry in addTable.values:
            command += f"\n {entry} {addTable.values[entry].GetSQLFormat()},"
        command = command[:len(command)-1]
        command += ")"
        
        # TODO: This feels a bit hacky.  Replace this in general with a function to check if the table exists.
        try:
            self.conn.execute(command)
        except:
            print("table already exists!")
        self.conn.commit()
        self.conn.close()

        self.tables.append(addTable)
    
    def getAllTables(self):
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

