# import the date 
from datetime import datetime, date

# program variables for task management program:
login = False
close = False
#------------------------------------------------------------------------------------------------------------------------------------------
existing_user = False
registered_user = False
#-------------------------------------------------------------------------------------------------------------------------------------------
task_owner = ""
task_title = ""
task_description = ""
task_assigned_date = ""
task_due_date = ""
task_completion = ""
#------------------------------------------------------------------------------------------------------------------------------------------

def reg_user():
    
# registration of a new user on program:

# registration will remain false until a new user is registered
    registered_user = False

# if statement is run if user selects "r" and the username == admin, meaning only a user with username - admin can register users
# file - user.txt - is opened,
# existing_user = False and will remain false unless new user being registered has same username as one currently on file
# user is requested to input a new username

    existing_user = False
    new_user = open("user.txt", 'r')       
    new_username = input("Please enter the new username for the new user: \n")
        
# if new_username == usernameTemp, this means that the chosen username for the new user attempting to be added is already on system
# if new_username == usernameTemp, existing_user would become True

    if new_username == usernameTemp:
        existing_user = True

# While loop is run while existing_user == True, 
# if existing_user == True, an error message will print saying that this username already exists, 
# user is then re-asked for a new username for the new user

    while existing_user == True:
        if new_username == usernameTemp:                    
            print("This username already exists, please enter another username: ")
            new_username = input("Please enter the new username for the new user: \n")
        else:
            existing_user = False
                     
# if new_username does not equal(!=) usernameTemp, the exisiting_user will remain false and a password for this new username will be requested
# user will be asked to confirm this new password for this new username 

    while existing_user == False:
        new_password = input("Please enter a new password: \n")
        confirm_new_password = input("Please confirm this new password: \n")

# values for new_password + confirm_new_password are compared to check if they are the same
# if statement is run to check if new_password == confirm_new_password, this will mean that the passwords are the same
# if passwords are the same this will be ammended to the - user.txt - file
# file character key then goes back to character[0] - in the file and the file is closed.

        if new_password == confirm_new_password:
            registered_user = True
            new_user = open("user.txt", 'a')
            new_user.write(f"{new_username}, {new_password}\n")
            print("\nNew user registered successfully")
        else:
            print("\nThe passwords entered do not match")
            new_user.seek(0, 0)
            new_user.close()
            break
        break 
                    
#------------------------------------------------------------------------------------------------------------------------------------------------           

def add_task():
    
# addition of a task on the program:
  
#  if loop is run if user selects "a"
# text file - tasks.txt - is opened and ammended
    
    new_task = open("tasks.txt", 'a+')

# as user has selected 'a' -- they will be prompted to answer questions and input data related to the task

    task_owner = input("Please confirm the username this task is assigned to: \n")
    task_title = input("Please confirm the title of the task: \n")
    task_description = input("Please enter a brief description of the task: \n")
    task_assigned_date = date.today()
    print(f"\nTask has been assigned to user on this date: {task_assigned_date} \n" )
    task_due_date = input("Please confirm when this task is due in the following format: yyyy-mm-dd \n")
    task_completion = input("Has this task been completed: Yes or No \n")

# once all the data is captured, this is ammended to the - tasks.txt file,
# it is ammended to the the - tasks.txt file - so that we add to and do no over-write the data already in the text file,
# a confirmation message is printed once this has been successfully added

    new_task.write(f"{task_owner}, {task_title}, {task_description}, {task_assigned_date}, {task_due_date}, {task_completion} ")
    print("New task has been successfully added to tasks.txt")
    new_task.close()

#-------------------------------------------------------------------------------------------------------------------------------------------------------

def view_all():
    

# if user has selected 'va'
# with/open block used to open and read text file - task.txt
# readlines() function is used to read the individual lines in the text file
# to read and display all tasks in text file, increment 'i' + range(len()) function is used, 
# increment 'i' + range(len()) function -- this calculates the total amount of characters in range
# 'i' is printed - which prints all users in the - user.txt - file

    with open('tasks.txt','r') as tasks:
        all_tasks = tasks.readlines()
        print("\n Displaying all user tasks :\n")
        for i in range(len( all_tasks)):
            print( all_tasks[i])
            break

#---------------------------------------------------------------------------------------------------------------------------------------------------------
def view_mine():                        # Checks the username to see their tasks 
    task_num = 1                        # Will be used to help the user identify what number each task is
    file = open("tasks.txt", "r")       # Opens the task file
    data = file.readlines()             # Reads all the lines
    data_new = []                       # Creates an empty list
    for num_list,data_list in enumerate(data, 1):      # Creates a for loop that splits our data up and enumerating them so we can select task numer

        if data_list.startswith(username):             # This checks if the username is in the user tasks folder

                    assigned_to, task, ds, dd, td, comp = data_list.strip(" ").strip("\n").split(",") # Splits the string up by "," so we can easily edit each value
                    
                    print(task_num)                                             # Prints the task number and and all details of the task
                    print(f"Assigned to\t\t\t|\t{assigned_to}")
                    print(f"Task\t\t\t\t|\t{task}")
                    print(f"Date Submitted\t\t|\t{ds}")
                    print(f"Due Date\t\t\t|\t{dd}")
                    print(f"Task Description\t|\t{td}")
                    print(f"Completed\t\t\t|\t{comp}")
                    print("")
                    task_num += 1                                               # Adds one task number so that the task number is not always one
    choice = int(input("enter the number of the task you want to display: "))   # Allows the user to select what task they want to change
    for num_list,data_list in enumerate(data, 1) :                              # We create another for loop to help us keep our data sorted


        if choice == num_list:                                                  # Checks if the user choice matchs any of the tasks
            print(data_list)


            print('#---------------------------------------------------------#') # Prints out a menu allowing user to edit task
            print('1 - Mark task as completed')
            print('2 - Edit Task')
            print('-1 - Return to Main Menu')
            print('#---------------------------------------------------------#')

            changes = int(input("Please enter an option: "))                    # Requests a user to enter a value of what they want to do
            data_list = data_list.strip()
            if changes == 1:                                                    # Checks if task is not completed

                if data_list.endswith("No"):                                    # Checks if the string ends with a no
                    data_list = data_list.strip(" ").strip("\n").split(",")     # Splits and strips the data
                    data_list[-1] = "Yes"                                       # Changes the last position in the string to yes
                    data_list = ", ".join(data_list)                            # Joins the strings together
                    data_new.append(data_list)                                  # Adds it into a new data list
                    print("Task completed")

            elif changes == 2:
                if data_list.endswith("Yes"):                           # Checks if the line ends with - Yes, if it does it means the task is complete and can't be edited
                    print("You can't edit a completed task.")

                else:
                    print('#--------------------------------------------------------#')   # Prints out a menu allowing user to edit task
                    print('1 - Edit Username')
                    print('2 - Edit Due Date')
                    print('#--------------------------------------------------------#')
                    edit_data = int(input("Please enter a value type: "))

                    if edit_data == 1:
                        new_name = input("Please enter the new user to handle the task: ")
                        data_list = data_list.strip(" ").strip("\n").split(",")         # Splits and strips the string
                        data_list[0] = new_name                                         # Checks the first position in the list and changes it to the new username
                        data_list = ", ".join(data_list)                                # Joins it into a string
                        data_new.append(data_list)                                      # Appends it into a new data structure
                        print("Username changed.")



                    elif edit_data == 2:

                        due_date_day = input("Please enter the day of the month it's due: ")
                        due_date_month = input("Please enter the numerical month it's due (eg. October = 10): ")
                        due_date_year = input("Please enter the year this is due: ")
                        new_date = f"{due_date_year}-{due_date_month}-{due_date_day}"   # Formats date inputs

                        data_list = data_list.strip(" ").strip("\n").split(",")         # Strips and splits the data
                        data_list[3] = new_date                                         # Changes the 4th position in the list with the new date



                        data_list = ", ".join(data_list)                            # Creates the new string
                        data_new.append(data_list)                                  # Adds the new data to the data
                        print("Task data modified completed")


                    else:
                        print("You entered an invalid response")
                        return view_mine()

            elif changes == -1:
                return selection(username)                              # If the user enters -1 it takes us back to login

        else:
            data_list = data_list.strip()
            data_new.append(data_list)

    with open("tasks.txt", "w") as file_write:
        for num_list in data_new:                                  # Takes the position the user entered at the start and enters it into the new data
            file_write.write(num_list+"\n")                        # Writes all the data in the ile

    file.close()                                                   # Closes the file
    return selection(username)
            
#---------------------------------------------------------------------------------------------------------------------------------------------------------


def show_statistics():
    
# option to review the statistics[all tasks] - only available to admin:
# if statement is used to check if the user selected "s" and if the admin is logged in {for view all tasks + view all users}

# with/open block used to open and read text file - task.txt
# readlines() function is used to read the individual lines in the text file
# to read and display all tasks in text file, increment 'i' + range(len()) function is used, 
# increment 'i' + range(len()) function -- this calculates the total amount of characters in range
# 'i' is printed - which prints all users in the - user.txt - file.


    with open('tasks.txt','r') as tasks:
        all_tasks = tasks.readlines()
        print("\nDisplaying all user tasks :\n")
        for i in range(len( all_tasks)):
            print(all_tasks[i])
            

# option to review the statistics[all users] - only available to admin:

# with/open block used to open and read text file - user.txt
# readlines() function is used to read the individual lines in the text file
# to read and display all tasks in text file, increment 'i' + range(len()) function is used,
# increment 'i' + range(len()) function -- this calculates the total amount of characters in range
# 'i' is printed - which prints all users in the - user.txt - file          

    with open('user.txt','r') as user_file:
        all_users = user_file.readlines()
        print("\nDisplaying all users :\n")
        for i in range(len(all_users)):
            print(all_users[i])
            

#---------------------------------------------------------------------------------------------------------------------------------------------------------
def generate_report():              #Checks the username to see their tasks [The username input will change as I create the finished product]

# -------------------------# Task Overview #------------------------------#
    # -----------------------# Total Tasks #-------------------------#
    
    file_task = open("tasks.txt", "r")              # Checks the tasks text document

    user_ov = open("user_overview.txt", "w")        # Opens the user overview file in write mode
    user_ov.truncate(0)                             # Resets the data
    user_ov.close()                                 # Closes the file

    task_data = open("task_overview.txt", "w")      # Opens the task overview file in write mode
    task_data.truncate(0)                           # Clears the file
    task_data.close()                               # Closes the file

    num_tasks = 0

    for line in file_task:                                      # Checks each line in the document
        if line != "\n":                                        # If it does not contain a new line, one is added
            num_tasks += 1                                      # Adds one to the total lines
    file_task.close()                                           # Closes the file

    to_1 = f"Total tasks: {num_tasks}"                          # Adds to the total_tasks

    # -----------------------------# Completed/incompleted Tasks #--------------------------------#
    
    total_comp = 0                                                          # Creates and empty variable
    total_incomp = 0                                                        # Creates an empty variable

    file = open("tasks.txt", "r")                                           # Opens a file

    data = file.readlines()                                                 # Reads all the lines

    for user_task in data:                                                  # Creates a for loop that reads the data
            data_split = user_task.strip(" ").strip("\n").split(",")        # Splits the data

            if data_split[5] == "Yes":                                      # Checks if there is any yes in the data
                total_comp += 1                                             # Adds one to the total comp

            elif data_split[5] == "No":                                     # Checks if there is a no in the data
                total_incomp += 1                                           # Adds one to the incomp

    to_2 = f"Total completed tasks: {total_comp}"
    to_3 = f"Total incompleted tasks: {total_incomp}"

    # -------------------------------------# Tasks overdue #---------------------------------#
    
    total_over_due = 0

    for due_dates in data:                                              # Creates a for loop


        data_split = due_dates.split(", ")                              # Splits the data
        due_date = "".join(data_split[4]).replace(" ", "")              # Converts it into a string
        past = datetime.strptime(due_date,"%d-%m-%Y")                   # Changes the date format
        present = datetime.now()                                        # Gets the current date

        if data_split[5] == "No":                                       # Checks if there is a no in the 5th psotion
            if past.date() > present.date():                            # Checks if the due date is larger than the current date
                total_over_due += 1


    to_4 = f"The total number of overdew tasks is: {total_over_due}"

    #-------------------------------# Total % of incomplete tasks #------------------------------#

    total_comp = 0
    total_incomp = 0
    total_inc_task_per = 0

    for incomplete_task_per in data:                                            # Creates a for loop


        data_split = incomplete_task_per.strip(" ").strip("\n").split(",")      # Splits the data up

        if " No" in data_split:                                                 # If there is a no in the data we add one to the total incomp
            total_incomp += 1

        elif " Yes" in data_split:                                              # If there is a yes we add one to the total completed
            total_comp += 1

        total_inc_task_per = total_incomp * 100 / (total_comp + total_incomp)   # Calculates the total percentage
                                                                                # incomp_task * 100 / total_of_tasks

    to_5 = f"The total percentage of incomplete tasks is: {total_inc_task_per}%" # % of incomplete tasks is printed
    
    # ---------------------------------# Total % of over_due tasks #---------------------------------#

    total_per_task_od = 0
    total_over_due = 0
    total_not_due = 0

    for due_dates in data:                                              # Creates a for loop


        data_split = due_dates.split(",")                               # Splits the data up
        due_date = data_split[3].replace(" ", "")                       # Removes any spacing in the data
        due_date = "".join(due_date)                                    # Joins the data into one string

        past = datetime.strptime(due_date, "%d-%m-%Y")                  # Formats how the date looks
        present = datetime.now()                                        # Gets current date


        if " No" in data_split[5]:                                      # If there is a no in the data
            if past < present:                                          # Checks if the past is greater than the present
                total_over_due += 1                                     # Adds one to the over due

        elif " Yes" in data_split[5]:                                   # Checks if there is a yes
            total_not_due += 1                                          # Adds one to the total not due

        total_per_task_od = int(total_over_due * 100 / (total_not_due + total_over_due))    # Calculates the percentage


    to_6 = f"The total percentage of overdue tasks is: {total_per_task_od}%"
# -------------------------------# User Data #-------------------------------------#
# ---------------------------# Counting users #----------------------------------#
    file = open("user.txt")

    num_of_users = 0

    for line in file:                                                                       # Creates a for loop that counts the lines in the file
        num_of_users += 1

    to_7 = f"Total number of users: {num_of_users}"                                         # Creates how many users in total there is


    with open("task_overview.txt", "a") as file_write:
        file_write.write(f"{to_1} \n {to_2} \n {to_3} \n {to_4} \n {to_5} \n {to_6} \n")    # Writes to the file

    file.close() # Closes the file
    
# ----------------------------------# Num Tasks assigned to each user #-----------------------------------#

    user=open("user.txt","r")
    user_task=open("tasks.txt","r")


    for line in user:                   # Creates a for loop that checks the user file
        username1 = line.split(", ")    # Splits it into a list
        user_print = username1[0]       # Gets the username we'll be printing
        user_task.seek(0)               # Seeks back to the start of the file

        total_tasks_for_user = 0        # All place holders for later use
        user_task_comp = 0
        user_task_incomp = 0
        over_due = 0



        for line2 in user_task:                              # For loop checking the tasks file

            username2 = line2.split(", ")                    # Splits the data up into a list
            user_strip = username2[4].replace(" ", "")
            past = datetime.strptime(user_strip,"%d-%m-%Y")  # Used to check if the due date is greater than todays date

            if username1[0] == username2[0]:    # Checks if the username matches the task
                total_tasks_for_user += 1       # Would you rather wait for me to get home and if it's still not fixed we can try again

                if username2[5] == " Yes":      # If the 5th option matches yes
                    user_task_comp += 1         # We add a value to completed data

                elif username2[5] == " No":     # If the data is no we add one to the value
                    user_task_incomp += 1       

                    if past > datetime.today() and username2[5] == " No":   # Checks if the task is over due
                        over_due += 1

        if total_tasks_for_user > 0:                                                                        # We check if the user has more than 1 task, as if they don't we can't calculate any stats
            per_of_task_to_user = (total_tasks_for_user / num_tasks) * 100                                  # All the calculations for % in the file
            total_per_comp = (total_tasks_for_user / 100) * user_task_comp                                  # Calculates the total % of completed tasks
            total_per_incomp = (total_tasks_for_user / (total_tasks_for_user - user_task_incomp)) * 100     # Calculates the total % of incomplete tasks
            total_over_due_user = (total_tasks_for_user / 100) * over_due                                   # Calculates the total of overdue tasks
        else:
            per_of_task_to_user = "No data."                # If the if statement finds no matches we will
            total_per_comp = "No data."                     # Write no data for each line of the users tasks
            total_per_incomp = "No data."                   # As there is no data to be calculated and read
            total_over_due_user = "No data."


        total_task1 = f"Total tasks: {total_tasks_for_user}"                                    # Writes out the data in a file
        total_task2 = f"Total % of tasks assigned to that user: {per_of_task_to_user}"
        total_task3 = f"Total % of tasks that are completed: {total_per_comp}"
        total_task4 = f"Total % of tasks that are incompleted: {total_per_incomp}"
        total_task5 = f"Total % of over_due tasks: {total_over_due_user}"
        total_task6 = username1[0]

        with open("user_overview.txt", "a") as file_write:                                  # Writes all the data out into the file
            file_write.write(f"{total_task6} \n {total_task1} \n {total_task2} \n {total_task3} \n {total_task4} \n {total_task5} \n")



    user.close()       # Closes the file
    user_task.close()  # Closes the file
    

#======================================================================================================================================
# Selection - function created to allow for different data to be displayed based on the user selection in Employee portal.

# once logged in, and if close remains false, meaning customer did not choose to exit employee portal,
# employee will have a list of options to choose from that is printed on the screen
# employee is prompted to select one of the options to continue
def selection(username):
    if login == True:
        while True:
            print("\nPlease select one of the following options: \n")
            if username == "admin":
                print("r - register user")
                print("a - add task")
                print("va - view all tasks")
                print("vm - view my task")
                print("gr - Generate report")
                print("ds - Display statistics ")
                print("e - exit")
                selection = input("\nPlease select one of the options in the menu above: ")


            else:
                print("a - add task")
                print("va - view all tasks")
                print("vm - view my task")
                print("e - exit")
                selection = input("\nPlease select one of the options in the menu above: ")


            break


    # if selection == e, Close will become True
    # and the user will exit the program and get a goodbye message.
    if selection == "e":
        close = True
        print("You have exited the portal, Goodbye!")


    # Admin option - Register user:
    if selection == "r" and username == "admin":
            reg_user()

    # Admin option - Generate reports:
    if selection == "gr" and username == "admin":
            generate_report()


    # Admin option - Show statistics:
    if selection == "ds" and username == "admin":
            show_statistics()


    # Adding a new tasks:
    elif selection == "a":
            add_task()


    # Option to view all Tasks:
    elif selection == "va":
            view_all()


    # Option to view my task/ tasks assigned to my name:
    elif selection == "vm":
            view_mine()

            
#==========================================================================================================================
# print default welcome message on company home page
print("Welcome to the company home page \n")
print("Please enter your login details to proceed \n")


# while loop is run, while - login is false and user has not yet logged in.
# user is asked to confirm both username and password

while login == False:
    user_file = open("user.txt", "r+")
    username = input("Please confirm your username \n")
    password = input("Please confirm your password \n")

# for loop is run in while loop to loop over data in - user.txt file
# users.txt - the white spaces at the beggining and end of the list are stripped using - line.strip() function
# variables - (usernameTemp + passwordTemp) - are created and assigned once the the username and password in file are split using - .split() function

    for line in user_file:
        line = line.strip()
        usernameTemp, passwordTemp = line.split(", ")
        
# if statement is run within the for loop to verify login details
# both username and password needs to be correct in order to login,
# the user input is verified against the variable values in - usernameTemp + passwordTemp,
# the usernameTemp + PasswordTemp variables are a readable format of the data contained in the text file - user.txt
# if username or password is incorrect, an error message is displayed
# if username and password are both correct, the user will login as login == True
# login will become "True" & the while loop will break and the user will be directed to the employee login page

        if username == usernameTemp and password == passwordTemp:
            login = True
            print("\n\nWelcome to the Employee portal \n\n")
            break

    if login == False:
        print("\nInvalid login details \n")
        while login == False:
            username = input("Please confirm your username \n")
            password = input("Please confirm your password \n")
    user_file.seek(0, 0)
    user_file.close()                                           # Closes the file
    selection(username)                                         # Employee goes to menu
