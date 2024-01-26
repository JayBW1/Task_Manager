# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password

#=====importing libraries===========
import os
from datetime import datetime, date
DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], \
DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], \
DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False
    task_list.append(curr_t)

#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")
# checks for respective text files, creates one if none exist        
if not os.path.exists("task_overview.txt"):
    with open("task_overview", "w") as task_overview:
        task_overview.write("Task Overview:\n")
if not os.path.exists("user_overview.txt"):
    with open("user_overview", "w") as user_overview:
        user_overview.write("User Overview:\n")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:
    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist\n")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password\n")
        continue
    else:
        print("Login Successful!\n")
        logged_in = True
        
def reg_user():
    '''Add a new user to the user.txt file'''
    # - Request input of a new username
    while True:
        new_username = input("New Username: ")
        usrtxt = open("user.txt")
        usrtxt = usrtxt.read()
        if new_username in usrtxt: # check if username already exists
            print("Username already in use")
            continue
        else:
            print("Valid username")
            break
    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
    # - If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[new_username] = new_password
        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))
    # - Otherwise you present a relevant message.
    else:
        print("Passwords do not match")

def add_task():
    '''Allow a user to add a new task to task.txt file
        Prompt a user for the following: 
         - A username of the person whom the task is assigned to,
         - A title of a task,
         - A description of the task and 
         - the due date of the task.'''
    while True:
        task_username = input("\nName of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
            continue
        else:
            break
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, \
DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }
    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.\n")

def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling)
    '''
    task_file = open("tasks.txt", "r+");task_file.seek(0,0)
    if  task_file.read() == "": # checks for tasks
        print("No Tasks Available\n");task_file.close()
    else:
        print("\nAll Task List:")
        for i, t in enumerate(task_list, 1):
            disp_str = f"Task:\t\t\t{t['title']}\n"
            disp_str += f"Assigned to:\t\t{t['username']}\n"
            disp_str += f"Date Assigned:\t\t{t['assigned_date'].strftime\
(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date:\t\t{t['due_date'].strftime\
(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Completed?\t\t{t['completed']}\n"
            disp_str += f"Task Description:\n {t['description']}\n"
            print(f"[{i}]\n{disp_str}")

file_rewrite = "" # declared variable

def view_mine():
    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling)
    '''
    task_file = open("tasks.txt", "r+");task_file.seek(0,0)
    if  task_file.read() == "": # check for tasks
        print("No Tasks Available\n");task_file.close()
    else:
        my_task_list = "" # declared variable
        print("\nMy Task List:\n")
        for i, t in enumerate(task_list, 1):
            if t['username'] == curr_user:
                disp_str = f"Task:\t\t\t{t['title']}\n"
                disp_str += f"Assigned to:\t\t{t['username']}\n"
                disp_str += f"Date Assigned:\t\t{t['assigned_date'].strftime\
    (DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Due Date:\t\t{t['due_date'].strftime\
    (DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Completed:\t\tNo\n"
                disp_str += f"Task Description:\n {t['description']}\n"
                print(f"[{i}]\n{disp_str}")
                my_task_list = my_task_list + f"\n[{i}]\n{disp_str}"
        current_entry = "my_task_menu" # splits loop into menus
        while True:
            if current_entry == "my_task_menu":
                vm_option1 = input("My Task Menu:\n[1] Select Task\n\
[-1] Main Menu\nSelect An Option: ")
                if vm_option1 == "-1":
                    print("Back To Main Menu\n");break
                elif vm_option1 == "1":
                    current_entry = "select_task"

            elif current_entry == "select_task":
                invalid = False # program loops if input is invalid
                vm_option2 = input("\nEnter Task Number: ")
                if vm_option2 == "-1":
                    print("Back To Main Menu\n")
                    break
                elif vm_option2 == "0":
                    print("Invalid Index");continue
                if invalid == False:
                    try: task_list[int(vm_option2) - 1]
                    except IndexError or ValueError:
                        print("Invalid Input");invalid = True
                    if invalid == False: # else loop until valid input
                        my_task_list = my_task_list.split("\n")
                        for index, first_line in enumerate(my_task_list):
                            if first_line == f"[{int(vm_option2)}]":
                                start = index # find start index
                        for index2, last_line in enumerate(my_task_list):
                            if f"[{int(vm_option2) + 1}]" not in my_task_list:
                                end = -1 # if end index does not exist
                            elif last_line == f"[{int(vm_option2) + 1}]":
                                end = index2 # find end index
                        global task_to_edit, old_task
                        task_to_edit = "";task_to_edit = list(task_to_edit)
                        old_task = "";old_task = list(old_task)
                        print("\nTask To Edit:")
                        vm_option2 = int(vm_option2)
                        for line in my_task_list[start:end]:
                            if line[:-1] == "":
                                break # uniform output
                            print(line)
                            line = line.replace("\t", "") # remove formatting
                            if f"[{vm_option2}]" in line:
                                continue # remove numbering for dict
                            else:
                                old_task.append(line)
                                task_to_edit.append(line)
                        task_description = "".join(old_task[-2 ::])
                        del(old_task[-2 ::]);del(task_to_edit[-2 ::])
                        old_task.append(task_description)
                        task_to_edit.append(task_description)
                        old_task_dict = dict(l.split(":") for l in old_task)
                        task_to_edit_dict = dict(l.split(":") \
                        for l in task_to_edit)
                        current_entry = "edit_task"

            elif current_entry == "edit_task":
                        vm_option3 = input("\nEdit Menu:\n[1] \
Mark Task As Completed\n[2] Edit Task\n[-1] Main Menu\nSelect Option: ")
                        if vm_option3 == "1":
                            new_task_list = []
                            if "Completed?\t\tYes" in task_to_edit:
                                print(f"new task list:\n{new_task_list}")
                                print("Task Already Marked As Completed")
                            else:
                                print(old_task_dict)
                                task_list.remove(old_task_dict)
                                print(old_task)
                                with open("tasks.txt", "w") as task_file:
                                    # new_task_list = []
                                    # for t in task_to_edit:
                                    #     str_attrs = [
                                    #         t['username'],
                                    #         t['title'],
                                    #         t['description'],
                                    #         t['due_date'].strftime(DATETIME_STRING_FORMAT),
                                    #         t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                                    #         "Yes" if t['completed'] else "No"
                                    #     ]
                                        # new_task_list.append(";".join(str_attrs))
                                    task_to_edit[5] = "Yes"
                                    new_task_list.append(task_list)
                                    new_task_list.append(";".join(task_to_edit))
                                    task_file.write("\n".join(new_task_list))
                                print(f"new task list:\n{new_task_list}")
                                print("Task Marked As Completed")
                        elif vm_option3 == "2":
                            task_list
                            add_task();print("Task Edited");continue
                        elif vm_option3 == "-1":
                            print("Back To Main Menu\n")
                            break
                        else:
                            print("Invalid Input\n")
            else:
                print("Invalid Input\n")
                
def generate_reports():
    with open("task_overview.txt", "r+") as task_overview:
        print(task_overview.read())
    with open("user_overview.txt", "r+") as user_overview:
        print(user_overview.read())

while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':reg_user()

    elif menu == 'a':add_task()

    elif menu == 'va':view_all()

    elif menu == 'vm':view_mine()
    
    elif menu == 'gr':generate_reports()

    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number
        of users and tasks.'''
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")