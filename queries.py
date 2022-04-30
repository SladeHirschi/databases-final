import sys
import sqlite3
from checkIsAdmin import check_Is_Admin
from getEmployeesByDepartment import get_Employees_By_Department
from getEmployeesByPosition import get_Employees_By_Position
from getEmployees import get_Employees
from moveEmployeeDepartment import move_Employee_Department
from moveEmployeePosition import move_Employee_Position

con = sqlite3.connect('database.db')
cur = con.cursor()

def getEmployeesByDepartment(department, position):
    get_Employees_By_Department(department, position, cur)

def getEmployeesByPosition(position):
    get_Employees_By_Position(position, cur)

def checkIsAdmin(admin):
    return check_Is_Admin(admin,cur)

def moveEmployeeDepartment(employee, department):
    move_Employee_Department(employee, department, cur)

def moveEmployeePosition(employee, position):
    move_Employee_Position(employee, position, cur)

def getEmployees():
    get_Employees(cur)

def printOptions():
    print("""
    What command would you like to do? 
        Possible: 
            getEmployees,
            getEmployeesByDepartment,
            getEmployeesByPosition,
            getDepartments, 
            getMembers, 
            getSupervisors, 
            getInventory,
            moveEmployee,
            movePosition
    
    To redisplay instructions enter 'HELP'
    To quit enter 'QUIT'
    """)

def getFunction():
    return input("What command would you like to do? ")


def main():
    printOptions()
    function = getFunction()
    while function != 'exit':
        if function == 'HELP':
            printOptions()
            function = getFunction()
        elif function == 'getEmployeesByDepartment':
            department = input("Which department? (tire_shop, front_end, produce, bakery, deli, night_merch, morning_merch, optical, hearing, pharmacy, meat, adminstration, food_court) ")
            getAllEmployeesByDepartment(department)
            function = getFunction()

        elif function == 'getEmployeesByDepartment':
            department = input("Which department? (tire_shop, front_end, produce, bakery, deli, night_merch, morning_merch, optical, hearing, pharmacy, meat, adminstration, food_court) ")
            getEmployeesByDepartment(department)
            function = getFunction()

        elif function == "moveEmployee":
            admin = input("What is your admin ID? ")
            isAdmin = checkIsAdmin(admin)
            # print(isAdmin)
            if admin == None:
                print("Sorry you need to provide and ID")
                function = getFunction()
            if isAdmin == True:
                employee = input("What employee is being moved? ")
                department = input("What department are they being moved too? ")
                moveEmployeeDepartment(employee,department)
            else:
                print("Sorry you have to be an Admin to move employees")
            function = getFunction()

        elif function == "movePosition":
            admin = input("What is your admin ID? ")
            isAdmin = checkIsAdmin(admin)
            if admin == None:
                print("Sorry you need to provide and ID")
                function = getFunction()
            if isAdmin == True:
                employee = input("What employee is being moved? ")
                position = input("What position are they being moved too? ")
                moveEmployeePosition(employee,position)
            else:
                print("Sorry you have to be an Admin to move employees")
            function = getFunction()
            

        elif function == 'addRelation':
            username1 = input("What is the username of your account? ")
            username2 = input("What is the username of the friend you want to add? ")
            addRelation(username1, username2)
            function = getFunction()

        elif function == 'viewPosts':
            viewPosts()
            position = input("What position? (employee, supervisor, admin) ")
            getEmployeesByDepartment(department, position)
            function = getFunction()

        elif function == 'getEmployeesByPosition':
            position = input("What position? (employee, supervisor, admin) ")
            getEmployeesByPosition(position)
            function = getFunction()

        elif function == 'getEmployees':
            getEmployees()
            function = getFunction()

        elif function == 'QUIT':
            break
        else:
            print("There is no function named " + function)
            function = getFunction()

main()
