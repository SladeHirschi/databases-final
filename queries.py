import sys
import sqlite3


con = sqlite3.connect('database.db')
cur = con.cursor()


def getFunction():
    return input("""
    What command would you like to do? 
        Possible: addUser, addAccount, viewAccounts, addRelation, viewPosts, addPost, addComment, addReply, likeComment, viewFriendsPosts)

    TO QUIT enter exit  
""")


def main():
    function = getFunction()
    while function != 'exit':
        if function == 'addUser':
            email = input("What is your email? ")
            addUser(email)
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
