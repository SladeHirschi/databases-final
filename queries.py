import sys
import sqlite3
<<<<<<< HEAD
from checkIsAdmin import check_Is_Admin
from getAllEmployeesByDepartment import get_All_Employees_By_Department
from getSupervisorsByDepartment import get_Supervisors_By_Department
from getEmployeesByDepartment import get_Employees_By_Department
from checkIsAdmin import check_Is_Admin

=======
from getEmployeesByDepartment import get_Employees_By_Department
from getEmployeesByPosition import get_Employees_By_Position
from getEmployees import get_Employees
>>>>>>> f9a8135f847a1bd7da2fcd7058b28d4b0a19fa31

con = sqlite3.connect('database.db')
cur = con.cursor()

def getEmployeesByDepartment(department, position):
    get_Employees_By_Department(department, position, cur)

def getEmployeesByPosition(position):
    get_Employees_By_Position(position, cur)

def checkIsAdmin(admin):
    return check_Is_Admin(admin,cur)

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
<<<<<<< HEAD
            getSupervisors, 
            getInventory,
            viewPosts, 
            addPost, 
            addComment, 
            addReply, 
            likeComment, 
            viewFriendsPosts,
            moveEmployee
=======
>>>>>>> f9a8135f847a1bd7da2fcd7058b28d4b0a19fa31

    TO quit enter 'QUIT'
""")


def main():
    function = getFunction()
    while function != 'exit':
        if function == 'getEmployeesByDepartment':
            department = input("Which department? (tire_shop, front_end, produce, bakery, deli, night_merch, morning_merch, optical, hearing, pharmacy, meat, adminstration, food_court) ")
<<<<<<< HEAD
            getAllEmployeesByDepartment(department)
            function = getFunction()

        elif function == 'getEmployeesByDepartment':
            department = input("Which department? (tire_shop, front_end, produce, bakery, deli, night_merch, morning_merch, optical, hearing, pharmacy, meat, adminstration, food_court) ")
            getEmployeesByDepartment(department)
            function = getFunction()

        elif function == "moveEmployee":
            admin = input("What is your admin ID? ")
            isAdmin = checkIsAdmin(admin)
            print(isAdmin)
            if admin == None:
                print("Sorry you need to provide and ID")
                function = getFunction()
            if isAdmin == True:
                employee = input("What employee is being moved? ")
                department = input("What department are they being moved too? ")
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
=======
            position = input("What position? (employee, supervisor, admin) ")
            getEmployeesByDepartment(department, position)
>>>>>>> f9a8135f847a1bd7da2fcd7058b28d4b0a19fa31
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
