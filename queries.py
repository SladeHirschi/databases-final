import sys
import sqlite3
from checkIsAdmin import check_Is_Admin
from getEmployeesByDepartment import get_Employees_By_Department
from getEmployeesByPosition import get_Employees_By_Position
from getEmployeesByDepartmentAndPosition import get_Employees_By_Department_And_Position
from getEmployees import get_Employees
from moveEmployeeDepartment import move_Employee_Department
from moveEmployeePosition import move_Employee_Position
from getMembers import get_Members
from getMembersByStatus import get_Members_By_Status
from changeMemberStatus import change_Member_Status
from getDetails import *

con = sqlite3.connect('database.db')
cur = con.cursor()

def getEmployeesByDepartment(department):
    get_Employees_By_Department(department, cur)

def getEmployeesByPosition(position):
    get_Employees_By_Position(position, cur)

def getEmployeesByDepartmentAndPosition(department, position):
    get_Employees_By_Department_And_Position(department, position, cur)

def checkIsAdmin(admin):
    return check_Is_Admin(admin,cur)

def moveEmployeeDepartment(employee, department):
    move_Employee_Department(employee, department, cur)

def moveEmployeePosition(employee, position):
    move_Employee_Position(employee, position, cur)

def getEmployees():
    get_Employees(cur)

def getMembers():
    get_Members(cur)

def getMembersByStatus(status):
    get_Members_By_Status(status, cur)

def changeMemberStatus(member, status):
    change_Member_Status(member, status, cur, con)

def getMemberDetails(member):
    get_Member_Details(member, cur)

def getEmployeeDetails(employee):
    get_Employee_Details(employee, cur)

def printOptions():
    print("""
    What command would you like to do? 
        Possible: 
            getEmployees,
            getEmployeesByDepartment,
            getEmployeesByPosition,
            getEmployeesByDepartmentAndPosition,
            moveEmployee,
            movePosition
            getMembers,
            getMembersByStatus,
            getEmployeeDetails,
            getMemberDetails,
            changeMemberStatus
    
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

        elif function == 'getEmployeesByPosition':
            position = input("What position? (employee, supervisor, admin) ")
            getEmployeesByPosition(position)
            function = getFunction()

        elif function == 'getEmployeesByDepartmentAndPosition':
            department = input("Which department? (tire_shop, front_end, produce, bakery, deli, night_merch, morning_merch, optical, hearing, pharmacy, meat, adminstration, food_court) ")
            position = input("What position? (employee, supervisor, admin) ")
            getEmployeesByDepartmentAndPosition(department, position)
            function = getFunction()

        elif function == 'getEmployees':
            getEmployees()
            function = getFunction()

        elif function == 'getMembers':
            getMembers()
            function = getFunction()

        elif function == 'getMembersByStatus':
            status = input("What status? (gold_star, business, executive) ")
            getMembersByStatus(status)
            function = getFunction()

        elif function == 'changeMemberStatus':
            admin = input("What is your admin ID? ")
            isAdmin = checkIsAdmin(admin)
            if admin == None:
                print("Sorry you need to provide and ID")
                function = getFunction()
            if isAdmin == True:
                member = input("What member is being changed? ")
                status = input("What status? (gold_star, business, executive) ")
                changeMemberStatus(member, status)
            else:
                print("Sorry you have to be an Admin to change member status")
            function = getFunction()

        elif function == 'getMemberDetails':
            member = input("What member? ")
            getMemberDetails(member)
            function = getFunction()

        elif function == 'getEmployeeDetails':
            employee = input("What employee? ")
            getEmployeeDetails(employee)
            function = getFunction()

        elif function == 'QUIT':
            break

        else:
            print("There is no function named " + function)
            function = getFunction()

main()
