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

def write_task_list():
    global task_list
    task_list = []
    with open("tasks.txt", 'r') as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]
    for t_str in task_data:
        curr_t = {}
        # Split by semicolon and manually add each component
        task_components = t_str.split(";")
        curr_t['username'] = task_components[0]
        curr_t['title'] = task_components[1]
        curr_t['description'] = f"{task_components[2]}"
        # remove strptime, item already formatted
        curr_t['due_date'] = task_components[3]
        curr_t['assigned_date'] = task_components[4]
        curr_t['completed'] = True if task_components[5] == "Yes" else False
        task_list.append(curr_t)
write_task_list()

def file_read_file_write():
    with open("tasks.txt", "r+") as task_file:
        task_file.seek(0,0)
        new_task_list = []
        str_attrs = []
        for item_value in values_to_edit_list:
            if str(item_value)[0] == " ":
                item_value = item_value[1:]
                str_attrs.append(item_value)
            else:
                str_attrs.append(item_value)
        new_task_list.append(";".join(str_attrs))
        task_lines = task_file.readlines()
        task_to_replace = task_lines[vm_option2 - 1]
        ready_task_list = []
        for line in task_lines:
            if line == task_to_replace:
                ready_task_list.append(new_task_list)
            else:
                ready_task_list.append(line)
    with open("tasks.txt", "w") as task_file:
        task_file.write("\n".join(new_task_list))

#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")
# task overview vars
if os.path.exists("task_overview.txt"):
    with open("task_overview.txt", "r") as task_overview:
        task_overview.seek(0, 0)
        task_overview_read = task_overview.readlines()
        for line in task_overview_read:
            if "Number Of Tasks Generated: " in line:
                line_search = line.split(" ")
                print(line_search)
                for file_number in line_search:
                    if file_number.isnumeric:
                        task_count = int(file_number)
                    else:continue
            if "Number Of Completed Tasks: " in line:
                line_search = line.split(" ")
                for file_number in line_search:
                    if file_number.isnumeric:
                        complete_task_count = int(file_number)
                    else:continue
            if "Number Of Incomplete Tasks: " in line:
                line_search = line.split(" ")
                for file_number in line_search:
                    if file_number.isnumeric:
                        incomplete_task_count = int(file_number)
                    else:continue
            if "Number Of Tasks Overdue: " in line:
                line_search = line.split(" ")
                for file_number in line_search:
                    if file_number.isnumeric:
                        overdue_task_count = int(file_number)
                    else:continue
            if "Percentage Of Tasks Inomplete: " in line:
                line_search = line.split(" ")
                for file_number in line_search:
                    if file_number.isnumeric:
                        task_complete_percentage = int(file_number)
                    else:continue
            if "Percentage Of Tasks Overdue: " in line:
                line_search = line.split(" ")
                for file_number in line_search:
                    if file_number.isnumeric:
                        task_overdue_percentage = int(file_number)
                    else:continue
else:
    task_count = 0
    complete_task_count = 0
    incomplete_task_count = task_count - complete_task_count
    overdue_task_count = 0
    try:task_complete_percentage = (incomplete_task_count / task_count) * 100
    except ZeroDivisionError:task_complete_percentage = 0
    try:task_overdue_percentage = (overdue_task_count / task_count) * 100
    except ZeroDivisionError:task_overdue_percentage = 0
# checks for respective text files, creates one if none exist
    task_overview = open("task_overview.txt", "w+")
    task_overview.write(f"Task Overview:\n\
Number Of Tasks Generated:\t\t{task_count} \n\
Number Of Completed Tasks:\t\t{complete_task_count} \n\
Number Of Incomplete Tasks:\t\t{incomplete_task_count} \n\
Number Of Tasks Overdue:\t\t{overdue_task_count} \n\
Percentage Of Tasks Inomplete:\t\t{task_complete_percentage} % \n\
Percentage Of Tasks Overdue:\t\t{task_overdue_percentage} %")
    task_overview.close()

# user overview vars
if os.path.exists("user_overview.txt"):
    with open("user_overview.txt", "r") as user_overview:
        user_overview.seek(0, 0)
        user_overview_read = user_overview.readlines()
        for line in user_overview_read:
            if "Number Of User Assigned Tasks: " in line:
                line_search = line.split(" ")
                for file_number in line_search:
                    if file_number.isnumeric:
                        user_task_count = int(file_number)
                    else:continue
            if "Percentage Of Total Tasks Assigned To User: " in line:
                line_search = line.split(" ")
                for file_number in line_search:
                    if file_number.isnumeric:
                        task_assigned_percentage = int(file_number)
                    else:continue
            if "Percentage Of Completed Tasks For User: " in line:
                line_search = line.split(" ")
                for file_number in line_search:
                    if file_number.isnumeric:
                        completed_assigned_task_percentage = int(file_number)
                    else:continue
            if "Percentage Of Incomplete Tasks For User: " in line:
                line_search = line.split(" ")
                for file_number in line_search:
                    if file_number.isnumeric:
                        incomplete_assigned_task_percentage = int(file_number)
                    else:continue
            if "Percentage Of Overdue Tasks For User: " in line:
                line_search = line.split(" ")
                for file_number in line_search:
                    if file_number.isnumeric:
                        overdue_assigned_task_percentage = int(file_number)
                    else:continue
else:
    user_task_count = 0
    user_complete_task_count = 0
    user_incomplete_task_count = 0
    user_overdue_task_count = 0
    try:task_assigned_percentage = (user_task_count / task_count) * 100
    except ZeroDivisionError:task_assigned_percentage = 0
    try:completed_assigned_task_percentage = \
            (user_complete_task_count / user_task_count) * 100
    except ZeroDivisionError:completed_assigned_task_percentage = 0
    try:incomplete_assigned_task_percentage = \
        (user_incomplete_task_count / user_task_count) * 100
    except ZeroDivisionError:incomplete_assigned_task_percentage = 0
    try:overdue_assigned_task_percentage = \
        (user_overdue_task_count / user_task_count) * 100
    except ZeroDivisionError:overdue_assigned_task_percentage = 0
    with open("user_overview.txt", "w+") as user_overview:
        user_overview.write(f"User Overview:\n\
Number Of User Assigned Tasks:\t\t\t{user_task_count} \n\
Percentage Of Total Tasks Assigned To User:\t{task_assigned_percentage} % \n\
Percentage Of Completed Tasks For User:\t\t\
{completed_assigned_task_percentage} % \n\
Percentage Of Incomplete Tasks For User:\t\
{incomplete_assigned_task_percentage} % \n\
Percentage Of Overdue Tasks For User:\t\t\
{overdue_assigned_task_percentage} %") # add username

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
    from datetime import date, datetime
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
        "due_date": due_date_time.strftime(DATETIME_STRING_FORMAT),
        "assigned_date": curr_date.strftime(DATETIME_STRING_FORMAT),
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
                t['due_date'],
                t['assigned_date'],
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    global task_count
    task_count += 1
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
            # removed strftime, item already formatted
            disp_str += f"Date Assigned:\t\t{t['assigned_date']}\n"
            disp_str += f"Due Date:\t\t{t['due_date']}\n"
            disp_str += f"Completed?\t\t{"Yes" if t['completed'] else "No"}\n"
            disp_str += f"Task Description:\n {t['description']}\n"
            print(f"[{i}]\n{disp_str}")

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
                # removed strftime, item already formatted
                disp_str += f"Date Assigned:\t\t{t['assigned_date']}\n"
                disp_str += f"Due Date:\t\t{t['due_date']}\n"
                disp_str += f"Completed?\t\t\
{"Yes" if t['completed'] else "No"}\n"
                disp_str += f"Task Description:\n {t['description']}\n"
                print(f"[{i}]\n{disp_str}")
                my_task_list = my_task_list + f"\n[{i}]\n{disp_str}"
        current_entry = "my_task_menu" # splits loop into menus
        while True:
            if current_entry == "my_task_menu": # my task menu
                vm_option1 = input("My Task Menu:\n[-1] Main Menu\n\
[1] Select Task\nSelect An Option: ")
                if vm_option1 == "-1":
                    print("Back To Main Menu\n");break
                elif vm_option1 == "1":
                    current_entry = "select_task"
                else:
                    print("Invalid Input\n")
            # select task menu
            elif current_entry == "select_task":
                invalid = False # program loops if input is invalid
                global vm_option2
                vm_option2 = input("\n[-1] Main Menu\n[0] Back\n\
Enter Task Number: ")
                if vm_option2.isnumeric():pass
                else:invalid = True;print("Invalid Input")
                if vm_option2 == "-1":
                    print("Back To Main Menu\n");break
                elif vm_option2 == "0":
                    print("Back To Previous Menu\n")
                    current_entry = "my_task_menu"
                elif invalid == False: # else loop until valid input
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
                            line = line.replace(" 00:00:00", "")
                            if "?" in line:
                                line = line.replace("?", ":")
                                old_task.append(line)
                                task_to_edit.append(line)
                            line = line.replace("\t", "") # remove formatting
                            if f"[{vm_option2}]" in line:
                                continue # remove numbering for dict
                            else:
                                old_task.append(line)
                                task_to_edit.append(line)
                         # join task description for dict
                        task_description = "".join(old_task[-2 ::])
                        del(old_task[-2 ::]);del(task_to_edit[-2 ::])
                        old_task.append(task_description)
                        task_to_edit.append(task_description)
                        old_task_dict = dict(l.split(":") for l in old_task)
                        global task_to_edit_dict, values_to_edit_list
                        task_to_edit_dict = dict(l.split(":")
                        for l in task_to_edit) # list => dict
                        values_to_edit_list = [] # list for appending
                        x_dict = {};values = []
                        for value in task_to_edit_dict.values():
                            values.append(value)
                        # order values accordingly
                        for x_dict in values:
                            x_dict = {}
                            x_dict = values[1]
                            values_to_edit_list.append(x_dict)
                            x_dict = values[0]
                            values_to_edit_list.append(x_dict)
                            x_dict = values[5]
                            values_to_edit_list.append(x_dict)
                            x_dict = values[3]
                            values_to_edit_list.append(x_dict)
                            x_dict = values[2]
                            values_to_edit_list.append(x_dict)
                            x_dict = values[4]
                            values_to_edit_list.append(x_dict)
                            break # one iteration
                        current_entry = "edit_task"
            # edit task menu
            elif current_entry == "edit_task":
                vm_option3 = input("\nEdit Menu:\n[-1] Main Menu\n\
[0] Back\n[1] Mark Task As Completed\n[2] Edit Task\nSelect Option: ")
                if vm_option3 == "-1":
                    print("Back To Main Menu\n");break
                elif vm_option3 == "0":
                    print("Back To Previous Menu")
                    current_entry = "select_task"
                elif vm_option3 == "1":
                    if values_to_edit_list[5] == "Yes":
                        print("Task Already Marked As Completed")
                    else:
                        values_to_edit_list[5] = "Yes"
                        file_read_file_write()
                        print("Task Marked As Completed")
                elif vm_option3 == "2":
                    if values_to_edit_list[5] == "Yes":
                        print("Completed Tasks Cannot Be Edited")
                    else:
                        edit_option1 = input("\nEdit Task:\n[-1] Main Menu\
[0] Back\n[1] Edit Assigned User\n[2] Edit Task Name\n\
[3] Edit Task Due Date\n[4] Edit Task Description\nSelect Option: ")
                        if edit_option1 == "-1":
                            print("Back To Main Menu\n");break
                        elif edit_option1 == "0":
                            print("Back To Previous Menu\n")
                            current_entry = "edit_task"
                        elif edit_option1 == "1":
                            task_user_input = input(f"\nPrevious Task User: \
{values_to_edit_list[0]}\nEnter New Task User: ")
                            with open("user.txt") as usrtx:
                                if task_user_input in usrtx:
                                    print(f"Task Assigned To \
{task_user_input}")
                                    values_to_edit_list[0] = task_user_input
                                    file_read_file_write()
                                else:
                                    print("Invalid Username\n")
                            
                        elif edit_option1 == "2":
                            task_name_input = input(f"\nPrevious Task Name: \
{values_to_edit_list[1]}\nEnter New Task Name: ")
                            values_to_edit_list[1] = task_name_input
                            print(f"Task Name Changed To {task_name_input}")
                            file_read_file_write()
                        elif edit_option1 == "3":
                            due_date_good = True
                            try:
                                task_due_date_input = input(f"\n\
Previous Task Due Date: {values_to_edit_list[3]}\nEnter New Task Due Date: ")
                                new_due_date_time = datetime.strptime\
(task_due_date_input, DATETIME_STRING_FORMAT)
                                break
                            except ValueError:
                                print("Invalid Datetime Format")
                                due_date_good = False
                            if due_date_good == True:
                                values_to_edit_list[3] = new_due_date_time
                                file_read_file_write()
                        elif edit_option1 == "4":
                            task_description_input = input(f"\n\
Previous Task Description: {values_to_edit_list[2]}\n\
Enter New Task Descrition: ")
                            values_to_edit_list[2] = task_description_input
                            file_read_file_write()
                            print(f"Task Description Changed To:\n\
{task_description_input}\n")
                        else:print("Invalid Input")
                else:
                    print("Invalid Input\n")
            else:
                print("Invalid Input\n")

def generate_reports():
    print("\nReports Generated\n")
    with open("task_overview.txt", "r+") as task_overview:
        print(f"{task_overview.read()}\n")
    with open("user_overview.txt", "r+") as user_overview:
        print(f"{user_overview.read()}\n")

while True:
    write_task_list()
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    menu = input('''Select one of the following Options below:
[r]\t- Registering a user
[a]\t- Adding a task
[va]\t- View all tasks
[vm]\t- View my task
[gr]\t- Generate reports
[ds]\t- Display statistics
[e]\t- Exit
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