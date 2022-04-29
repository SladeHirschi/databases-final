import sys
import sqlite3
from getEmployeesByDepartment import get_Employees_By_Department
from getEmployeesByPosition import get_Employees_By_Position
from getEmployees import get_Employees

con = sqlite3.connect('database.db')
cur = con.cursor()

def getEmployeesByDepartment(department, position):
    get_Employees_By_Department(department, position, cur)

def getEmployeesByPosition(position):
    get_Employees_By_Position(position, cur)

def getEmployees():
    get_Employees(cur)

def getFunction():
    return input("""
    What command would you like to do? 
        Possible: 
            getEmployees,
            getEmployeesByDepartment,
            getEmployeesByPosition,
            getDepartments, 
            getMembers, 

    TO quit enter 'QUIT'
""")


def main():
    function = getFunction()
    while function != 'exit':
        if function == 'getEmployeesByDepartment':
            department = input("Which department? (tire_shop, front_end, produce, bakery, deli, night_merch, morning_merch, optical, hearing, pharmacy, meat, adminstration, food_court) ")
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
