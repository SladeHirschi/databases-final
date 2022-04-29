import sys
import sqlite3
from getAllEmployeesByDepartment import get_All_Employees_By_Department
from getSupervisorsByDepartment import get_Supervisors_By_Department
from getEmployeesByDepartment import get_Employees_By_Department


con = sqlite3.connect('database.db')
cur = con.cursor()

def getSupervisorsByDepartment(department):
    get_Supervisors_By_Department(department, cur)
    
def getAllEmployeesByDepartment(department):
    get_All_Employees_By_Department(department, cur)

def getEmployeesByDepartment(department):
    get_Employees_By_Department(department, cur)

def getEmployees():
    print("getting employees")

def getFunction():
    return input("""
    What command would you like to do? 
        Possible: 
            getEmployees,
            getSupervisors,
            getAdmins,
            getAllEmployees,
            getAllEmployeesByDepartment, 
            getEmployeesByDepartment, 
            getDepartments, 
            getSupervisorsByDepartment, 
            getMembers, 
            getSupervisors, 
            getInventory,
            viewPosts, 
            addPost, 
            addComment, 
            addReply, 
            likeComment, 
            viewFriendsPosts

    TO quit enter 'QUIT'
""")


def main():
    function = getFunction()
    while function != 'exit':
        if function == 'getSupervisorsByDepartment':
            department = input("Which department? (tire_shop, front_end, produce, bakery, deli, night_merch, morning_merch, optical, hearing, pharmacy, meat, adminstration, food_court) ")
            getSupervisorsByDepartment(department)
            function = getFunction()

        elif function == 'getAllEmployeesByDepartment':
            department = input("Which department? (tire_shop, front_end, produce, bakery, deli, night_merch, morning_merch, optical, hearing, pharmacy, meat, adminstration, food_court) ")
            getAllEmployeesByDepartment(department)
            function = getFunction()

        elif function == 'getEmployeesByDepartment':
            department = input("Which department? (tire_shop, front_end, produce, bakery, deli, night_merch, morning_merch, optical, hearing, pharmacy, meat, adminstration, food_court) ")
            getEmployeesByDepartment(department)
            function = getFunction()

        elif function == 'addRelation':
            username1 = input("What is the username of your account? ")
            username2 = input("What is the username of the friend you want to add? ")
            addRelation(username1, username2)
            function = getFunction()

        elif function == 'viewPosts':
            viewPosts()
            function = getFunction()

        elif function == 'addPost':
            username = input("What is your username? ")
            content = input("What do you want to write in your post? ")
            addPost(username, content)
            function = getFunction()

        elif function == 'viewFriendsPosts':
            username = input("What is your username? ")
            viewFriendsPosts(username)
            function = getFunction()

        elif function == 'QUIT':
            break
        else:
            print("There is no function named " + function)
            function = getFunction()

main()
