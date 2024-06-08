# To Do List

import pandas as pd

tasks_list = []


def view_task():
    if len(tasks_list) == 0 or df.empty:
        print("Task List is empty")
        print("Try adding some tasks and try again!")
    else:
        print(df)
        
def create_task():
    inp = input("Enter Task: ")
    tasks_list.append(inp)
    print("Task successfully added in task list")

def remove_task():
    rm_inp = int(input("Enter task number of a task to remove it from tasks list: "))
    df.drop(rm_inp, inplace = True)
    print(f"Task number {rm_inp} is removed successfully")
    


#User choice
while True:


    print("\n===Available Choices===")
    print("1. View Tasks List")
    print("2. Create Task")
    print("3. Remove a Task")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        view_task()
    elif choice == '2':
        create_task()
        df = pd.DataFrame(tasks_list)
        df.columns = ["Tasks"]
    elif choice == '3':
        remove_task()
    elif choice == '4':
        exit()
    else:
        print("Invalid choice!!! Try again")
