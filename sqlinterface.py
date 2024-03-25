import sqlite3 as sql

class DataBase():
    tables : list
    def __init__(self, dbName : str) -> None:
        self.dbName = dbName
        self.tables = []
    
    def initDataBase(self):
        self.conn = sql.connect(self.dbName)
    
    def createTable(self, addTable):
        self.initDataBase()

        command = f"CREATE TABLE {addTable.name} ("

        for entry in addTable.values:
            command += f"\n {entry} {addTable.values[entry].GetSQLFormat()},"
        command = command[:len(command)-1]
        command += ")"

        print(command)
        
        try:
            self.conn.execute(command)
        except:
            print("table already exists!")
        self.conn.commit()
        self.conn.close()

        self.tables.append(addTable)


class Table():
    name : str = ""
    values : dict
    def __init__(self, name, values) -> None:
        self.name = name
        self.values = values

class SQLValue:
    def GetSQLFormat(self) -> str:
        return ""

class VarChar(SQLValue):
    def __init__(self, val : int) -> None:
        self.val = val
    
    def GetSQLFormat(self) -> str:
        return f"varchar({self.val})"
    
class Int(SQLValue):
    def GetSQLFormat(self) -> str:
        return "Int"

