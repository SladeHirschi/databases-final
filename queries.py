import sys
import sqlite3


con = sqlite3.connect('database.db')
cur = con.cursor()

def getManagersByDepartment(department):
    data1 = cur.execute("SELECT id FROM accounts WHERE username = ?", [username])
    accountId = data1.fetchone()
    if accountId is not None:
        id = accountId[0]
    else:
        print("This is an invalid username")
        return
    data = cur.execute("""
        SELECT 
            p.content, 
            p.likes, 
            p.dislikes,
            a1.username as poster,
            a2.username as commenter,
            c.content
        FROM 
            posts p
        LEFT JOIN
            accounts a1
            ON p.account_id = a1.id
        LEFT JOIN
            comments c
            ON c.post_id = p.id
        LEFT JOIN
            accounts a2
            ON c.account_id = a2.id
        JOIN
            friends f
            ON f.from_id = ? AND p.account_id = f.to_id
        ORDER BY a1.username
        """, [id])
    posts = data.fetchall()
    print(posts)
    for post in posts:
        if post is None:
            print("There are none")
            return
        else:
            print("""
                Posted By: {}
                    Content: {}
                Comments:
                    {}
                    Commented By: {}
                Likes {}  Dislikes {}
            """.format(post[3], post[0], post[5], post[4], post[1], post[2]))

def getFunction():
    return input("""
    What command would you like to do? 
        Possible: getEmployees, getEmployeesByDepartment, getDepartments, getManagersByDepartment, getMembers, getSupervisors, getInventory, viewPosts, addPost, addComment, addReply, likeComment, viewFriendsPosts)

    TO QUIT enter 'exit'
""")


def main():
    function = getFunction()
    while function != 'exit':
        if function == 'getManagersByDepartment':
            department = input("Which department? (tire shop, front end, produce, bakery, deli, night merch, morning merch, optical, hearing, pharmacy, meat, adminstration, food court) ")
            getManagersByDepartment(department)
            function = getFunction()

        elif function == 'addAccount':
            email = input("What is the email associated with the account you want to create? ")
            username = input("What do you want your username to be? ")
            password = input("What is your password? ")
            addAccount(email, username, password)
            function = getFunction()

        elif function == 'viewAccounts':
            viewAccounts()
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

        elif function == 'exit':
            break

        else:
            print("There is no function named " + function)
            function = getFunction()

main()
