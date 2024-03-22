# username: admin | password: password
from datetime import date, datetime
import os
DTF = "%Y-%m-%d"

# Create files if non exist
if not os.path.exists("user.txt"):
    with open("user.txt", "w+") as f:
        f.write("admin;password")

if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w+"):
        pass

# ==== user section ====
logged_in = False; logged = []; logged.append(logged_in)
username_password = {}; curr_user = []
def login(input_name: str, input_pass: str):
    """Checks if user input is correct and logs in if correct."""
    with open("user.txt", "r") as f:
        f_read = f.read()
    user_data = f_read.split("\n")
    for user in user_data:
        username, password = user.split(";")
        username_password[username] = password
    # check username
    if input_name in username_password.keys():
        pass
    else:
        return "Invalid Username"
    # check password
    if username_password[input_name] == input_pass:
        logged[0] = True; curr_user.append(input_name)
        return "Login Successful\n"
    else:
        return "Invalid Password"

def reg_user(new_user: str, new_pass: str):
    """Adds new user details to user file."""
    new_reg = f"{new_user};{new_pass}"
    with open("user.txt", "a") as f:
        f.write(f"\n{new_reg}")

# ==== task section ====
def add_task(
    assigned_user: str, task_name: str, desciption: str,
    due_date: date):
    """Takes inputs, creates task line and appends to task file."""
    curr_date = date.today()
    completed = False
    new_task = f"{assigned_user};{task_name};{desciption}\
;{due_date};{curr_date};{completed}"
    with open("tasks.txt", "a") as f:
        f.write(new_task + "\n")

def write_task_file(list1 : list, file1):
    """Reads tasks from task_list, formats and writes to file."""
    with open(file1, "w") as f:
        for task in list1:
            task_str = ""
            task_str += f"{task['username']};{task['title']};\
{task['description']};{task['due_date']};{task['assigned_date']};\
{task['completed']}"
            f.write(task_str + "\n")

def write_task_list(file1) -> list:
    """Reads tasks.txt data and appends to task list."""
    curr_t = {}; task_list = []
    with open(file1, "r") as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]
        
        if task_data == []:
            pass
        
        else:
            for t_str in task_data:
                curr_t = {}
                # Split by semicolon and add each component
                task_components = t_str.split(";")
                curr_t['username'] = task_components[0]
                curr_t['title'] = task_components[1]
                curr_t['description'] = task_components[2]
                curr_t['due_date'] = task_components[3]
                curr_t['assigned_date'] = task_components[4]
                curr_t['completed'] = task_components[5]
                task_list.append(curr_t)
    return task_list

def view_mine(list1: list) -> str:
    """Reads the task from tasks.txt file and prints to the console in the
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling).
    [VM] - User can then select a task to edit or mark as complete."""
    disp_str = ""
    task_count = 0; my_task_count = 0
    if list1 == []: # check for tasks
        disp_str = "No Tasks Available"

    else:
        for i, t in enumerate(list1, 1):
            task_count += 1
            if t['username'] == curr_user[0]:
                my_task_count += 1
                alignment_list.append(f"{my_task_count};{task_count}")
                disp_str += f"Task [{i}]:\t\t{t['title']}\n"
                disp_str += f"Assigned to:\t\t{t['username']}\n"
                disp_str += f"Date Assigned:\t\t{t['assigned_date']}\n"
                disp_str += f"Due Date:\t\t{t['due_date']}\n"
                disp_str += f"Completed?\t\t{'Yes' if t['completed'] == 'True' else 'No'}"
                disp_str += f"\nTask Description:\n {t['description']}\n\n"
                
        if disp_str == "":
            disp_str = "No Tasks Available"
    return disp_str

def view_all(list1: list) -> str:
    """Reads the task from tasks.txt file and prints to the console in the 
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling)."""
    disp_str = ""
    if list1 == []: # check for tasks
        disp_str = "No Tasks Available"

    else:
        for i, t in enumerate(list1, 1):
            disp_str += f"Task [{i}]:\t\t{t['title']}\n"
            disp_str += f"Assigned to:\t\t{t['username']}\n"
            disp_str += f"Date Assigned:\t\t{t['assigned_date']}\n"
            disp_str += f"Due Date:\t\t{t['due_date']}\n"
            disp_str += f"Completed?\t\t{'Yes' if t['completed'] == 'True' else 'No'}"
            disp_str += f"\nTask Description:\n {t['description']}\n\n"
    return disp_str

# ==== overview reports ====
def generate_reports(list1 : list) -> str:
    """Read task list, count values for output,
    format data for documentation."""
    task_count = len(list1)
    complete_count = 0
    overdue_count = 0
    
    for t in list1:
        if t['completed'] == "True":
            complete_count += 1
        if datetime.strptime(t['due_date'], DTF).date() < date.today():
            overdue_count += 1
            
    incomplete_count = task_count - complete_count
    
    try:
        incomplete_percentage = (100 // task_count) * incomplete_count
        overdue_percentage = (100 // task_count) * overdue_count
    except ZeroDivisionError:
        incomplete_percentage = 0
        overdue_percentage = 0
        
    # overview_format
    all_data_str = f"Task Overview:\n\
Number Of Tasks Generated:\t\t{task_count}\n\
Number Of Completed Tasks:\t\t{complete_count}\n\
Number Of Incomplete Tasks:\t\t{incomplete_count}\n\
Number Of Tasks Overdue:\t\t{overdue_count}\n\
Percentage Of Tasks Incomplete:\t\t{incomplete_percentage} %\n\
Percentage Of Tasks Overdue:\t\t{overdue_percentage} %\n\n"

    with open("task_overview.txt", "w+") as f:
        f.write(all_data_str)

    def format_user(dict1 : dict) -> str:
        """Formats dict components into a string for user documentation"""
        try:
            task_assigned_percentage = (
                100 // task_count) * int(dict1['task_count'])
            user_completed_percentage = (
                100 // int(
                    dict1['task_count'])) * int(dict1['complete_count'])
            user_incomplete_percentage = (
                100 // int(dict1['task_count'])) * (
                    int(dict1['task_count']) - int(dict1['complete_count']))
            user_overdue_percentage = (
                100 // int(
                    dict1['task_count'])) * int(user_dict['overdue_count'])
        
        except ZeroDivisionError:
            task_assigned_percentage = 0
            user_completed_percentage = 0
            user_incomplete_percentage = 0
            user_overdue_percentage = 0

        user_data_str = f"{dict1['username']} Overview:\n\
Number Of User Assigned Tasks:\t\t\t{dict1['task_count']}\n\
Percentage Of Total Tasks Assigned To User:\t{task_assigned_percentage} %\n\
Percentage Of Completed Tasks For User:\t\t{user_completed_percentage} %\n\
Percentage Of Incomplete Tasks For User:\t{user_incomplete_percentage} %\n\
Percentage Of Overdue Tasks For User:\t\t{user_overdue_percentage} %\n\n"
        return user_data_str
    
    all_user_data_str = f"User Overview:\n\
Number Of Registered Users:\t\t{len(username_password.keys())}\n\
Number Of Tasks Generated:\t\t{task_count}\n\n"

    username_list = username_password.keys()
    username_list = list(username_list)
    for i in range(len(username_list)):
        user_dict = {"username" : "",
                    "task_count" : 0,
                    "complete_count" : 0,
                    "overdue_count" : 0
                    }
        user_dict['username'] = username_list[i]
        
        for t in list1:
            if user_dict['username'] == t['username']:
                user_dict['task_count'] += 1
            if user_dict['username'] == t['username']\
                and t['completed'] == 'True':
                user_dict['complete_count'] += 1
            if user_dict['username'] == t['username']\
                and t['completed'] == 'False'\
                and datetime.strptime(
                    t['due_date'], DTF).date() < date.today():
                user_dict['overdue_count'] += 1
                
        all_data_str += format_user(user_dict)
        all_user_data_str += format_user(user_dict)
        
    with open("user_overview.txt", "w+") as f:
        f.write(all_user_data_str)
        
    return all_data_str

# ==== main loop ====
while True:
    alignment_list = []

    if logged[0] == False:
        curr_user = []
        print("\nLogin")
        username = input("Username: ")
        password = input("Password: ")
        print(login(username, password))

    else:
        menu = input('''Main Menu:
[R]\t- Registering A User
[A]\t- Adding A Task
[VA]\t- View All Tasks
[VM]\t- View My Task
[GR]\t- Generate Reports
[DS]\t- Display Statistics
[LO]\t- Log Out
[E]\t- Exit
: ''').lower()

        if menu == "r":
            print("\nRegister User:")
            while True:
                new_user = input("Enter Username: ")
                if new_user in username_password.keys():
                    print("Username Already In Use")
                else:
                    print("Valid Username")
                    new_pass = input("Enter Password: ")
                    confirm = input("Enter Password Again: ")
                    if confirm == new_pass:
                        print(f"{new_user} Registered\n")
                        print(
                        "Please Log Out And Log Back In For Updated Reports")
                        reg_user(new_user, new_pass)
                        break

        elif menu == "a":
            print("\nAdding Task:"); done = False
            while True:
                assigned_user = input("Enter User: ")
                
                if assigned_user not in username_password.keys():
                    print("Invalid Username")
                else:
                    task_name = input("Enter Task Name: ")
                    description = input("Enter Description: ")
                    
                    due_date = input("Enter Due Date (YYYY-MM-DD): ")
                    try:
                        due_date = datetime.strptime(due_date, DTF).date()
                        done = True
                    except ValueError:
                        print("Invalid Date\n")

                    if done == True:
                        add_task(
                            assigned_user, task_name, description, due_date)
                        print("Task Added\n"); break

        elif menu == "va":
            print(f"\nView All Tasks:\n\n{view_all(write_task_list('tasks.txt'))}")

        elif menu == "vm":
            print(f"\nView All Tasks:\n\n{view_all(write_task_list('tasks.txt'))}")
            # align_list => align_dict
            align_dict = dict(str(l).split(";") for l in alignment_list)
            # align_dict used to replace task in task list
            # in relation to my tasks
            if view_mine(write_task_list("tasks.txt")) == "No Tasks Available":
                pass

            else:
                while True:
                    vm_menu_1 = input(
                        "Select Task:\n[-1] Main Menu\nEnter Task Number: ")

                    if vm_menu_1 == "-1":
                        print("Back To Main Menu\n"); break

                    elif vm_menu_1.isnumeric():
                        if vm_menu_1 in align_dict.values():
                            print(f"Task {vm_menu_1} Selected\n")
                            
                            vm_menu_2 = input(
"""Edit Task:\n\
[-1] Main Menu\n\
[1] Mark As Completed\n\
[2] Edit Assigned User\n\
[3] Edit Due Date\n\
Enter: """)
                            
                            if vm_menu_2 == "-1":
                                print("Back To Main Menu\n"); break
                            
                            elif vm_menu_2.isnumeric():
                                new_task_list = write_task_list("tasks.txt")
                                
                                if new_task_list[int(vm_menu_1) - 1]\
                                        ['completed'] == True:
                                    print("Can't Edit Completed Tasks")
                                
                                else:
                                    if vm_menu_2 == "1":
                                        new_task_list[int(vm_menu_1) - 1]\
                                        ['completed'] = True

                                        print(
                                    f"Task {vm_menu_1} Marked As Completed\n")
                                        write_task_file(
                                            new_task_list, "tasks.txt")
                                        
                                    elif vm_menu_2 == "2":
                                        edit_user = input(
                                        "\nEnter New Assigned User: ")
                                        
                                        new_task_list[int(vm_menu_1) - 1]\
                                            ['username'] = edit_user
                    
                                        print("Assigned User Edited\n")
                                        write_task_file(
                                            new_task_list, "tasks.txt")
                                        
                                    elif vm_menu_2 == "3":
                                        edit_date = input(
                                        "\nEnter New Due Date (YYYY-MM-DD): ")
                                        try:
                                            edit_date = datetime.strptime(
                                                edit_date, DTF).date()
                                            done = True
                                        except ValueError:
                                            print("Invalid Date\n")
                                        
                                        if done == True:
                                            new_task_list[int(vm_menu_1) - 1]\
                                                ['due_date'] = edit_date
                        
                                            print("Due Date Edited\n")
                                            write_task_file(
                                                new_task_list, "tasks.txt")
                                    
                                    else:
                                        print("Invalid Input\n")
                                    
                            else:
                                print("Invalid Input\n")

                        else:
                            print("Invalid Input\n")

                    else:
                        print("Invalid Input\n")

        elif menu == "gr":
            print(
                f"\nReports Generated\n\n{generate_reports(
                    write_task_list("tasks.txt"))}")
        
        elif menu == "ds" and curr_user[0] == 'admin':
            # If user is admin, display stats about number of users and tasks
            print(f"\n-----------------------------------")
            print(f"Number Of Users: \t\t {len(username_password.keys())}")
            print(f"Number Of Tasks: \t\t {len((write_task_list("tasks.txt")))}")
            print("-----------------------------------")
        
        elif menu == "lo":
            print(f"{curr_user[0]} Logged Out"); logged[0] = False
        
        elif menu == "e":
            print("Goodbye"); exit()
            
        else:
            print("Invalid Input")