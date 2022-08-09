# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# KDoehlert,8.8.2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
try:
    objFile = open("ToDoList.txt", "r")
    for row in objFile:
        lstRow = row.split(",") # Returns a list!
        dicRow = {"Task":lstRow[0],"Priority":lstRow[1].strip()}
        lstTable.append(dicRow)
    objFile.close()
    print("Data retrieved from file.")
except:
    print("File not found, will make new file when you save.")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        print("Your current To Do list is:\n")
        for row in lstTable:
            strData = ("Task: " + row["Task"] + "\nPriority: " + row["Priority"] +"\n")
            print(strData)
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        strTask = input("Enter a Task to add: ")
        strPriority = input("Enter the Priority: ")
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        print("\nItem added.")
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        strTask = input("Task to remove: ")
        for row in lstTable:
            if row["Task"].lower() == strTask.lower():
                del lstTable[lstTable.index(row)]
                print("\nItem removed.")
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(row["Task"] + "," + row["Priority"] + "\n")
        objFile.close()
        print("File saved.")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        strSave = input("Would you like to save your data? [y or n]: ")
        if strSave.lower() == "y":
            objFile = open("ToDoList.txt", "w")
            for row in lstTable:
                objFile.write(row["Task"] + "," + row["Priority"] + "\n")
            objFile.close()
            print("File saved. Goodbye")
        else:
            print("Goodbye.")
        break  # and Exit the program
