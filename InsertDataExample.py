from sqlinterface import *
import sqlinterface

def main():
    sqlinterface.printDebugMessage = True
    db = DataBase("crosscountry.db")

    # Table holds the name of the table and then a dictionary containing the value name and type
    userTable = Table("Users", {"UserCode" : VarChar(10), "LastName" : VarChar(25), "House" : VarChar(10), "Role" : VarChar(10), "YearLevel" : Int(), "DOB" : VarChar(8), "FirstName" : VarChar(20)})

    # NOTE: This may change in the future!  I don't particuarly enjoy how this works
    db.insertIntoTable(userTable, ["p2242", "Yapper", "Morgan", "Teacher", "29", "7/2001", "Dallas"])
    

if __name__ == '__main__':
    main()