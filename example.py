from sqlinterface import *


def main():
    db = DataBase("crosscountry.db")
    userTable = Table("Users", {"UserCode" : VarChar(10), "LastName" : VarChar(25), "House" : VarChar(10), "Role" : VarChar(10), "YearLevel" : Int(), "DOB" : VarChar(8), "FirstName" : VarChar(20)})
    db.createTable(userTable)

    AgeLevelTable = Table("AgeLevel", {"AgeLevel" : VarChar(10), "UserCode" : VarChar(10)})
    db.createTable(AgeLevelTable)

    AgeLevelEventTable = Table("AgeLevelEvent", {"AgeLevel" : VarChar(10), "UserCode" : VarChar(10), "EventName" : VarChar(20)})
    db.createTable(AgeLevelEventTable)

    AgeLevelEventPlaceTable = Table("AgeLevelEventPlace", {"AgeLevel" : VarChar(10), "UserCode" : VarChar(10), "EventName" : VarChar(20), "Time" : VarChar(6), "Place" : Int(), "Points" : Int()})
    db.createTable(AgeLevelEventPlaceTable)
    

if __name__ == '__main__':
    main()