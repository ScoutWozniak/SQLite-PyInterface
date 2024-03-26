from sqlinterface import *
import sqlinterface

def main():
    sqlinterface.printDebugMessage = True
    db = DataBase("crosscountry.db")

    # Table holds the name of the table and then a dictionary containing the value name and type
    userTable = Table("Users", {"UserCode" : VarChar(10), "LastName" : VarChar(25), "House" : VarChar(10), "Role" : VarChar(10), "YearLevel" : Int(), "DOB" : VarChar(8), "FirstName" : VarChar(20)})
    # Passing the table into the actual database will create it in SQL
    # NOTE: If the table already exists in python this won't do anything
    db.createTable(userTable)

    AgeLevelTable = Table("AgeLevel", {"AgeLevel" : VarChar(10), "UserCode" : VarChar(10)})
    db.createTable(AgeLevelTable)

    AgeLevelEventTable = Table("AgeLevelEvent", {"AgeLevel" : VarChar(10), "UserCode" : VarChar(10), "EventName" : VarChar(20)})
    db.createTable(AgeLevelEventTable)

    AgeLevelEventPlaceTable = Table("AgeLevelEventPlace", {"AgeLevel" : VarChar(10), "UserCode" : VarChar(10), "EventName" : VarChar(20), "Time" : VarChar(6), "Place" : Int(), "Points" : Int()})
    db.createTable(AgeLevelEventPlaceTable)

    db.insertIntoTable(userTable, ["s624881", "McCarney", "Morgan", "Student", "2024", "testdate", "Dallas"])
    

if __name__ == '__main__':
    main()