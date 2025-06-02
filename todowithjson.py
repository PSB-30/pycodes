import json
import os

todo_list=[]

def save_tasks():
    with open("tasks.json","w")as file:
        json.dump(todo_list,file)

def load_task():
    global todo_list
    try:
        with open("tasks.json","r") as file:
            todo_list=json.load(file)
    except FileNotFoundError:
        todo_list=[]

def add(task,priority):
    todo_list.append({"task":task,"priority":priority})
    print(f"The {task}  and Priority {priority} have been added to the list..!!")

def view():
    if not todo_list:
        print("No task to show")
        load_task()
    else:
        print("Here are the tasks..!!!")
        sorted_tasks = sorted(todo_list, key=lambda x: x['priority'])
        for x,item in enumerate(sorted_tasks,start=1):
            print(f"{x}. {item['task']} (priority: {item['priority']})")


def remove(task):
    if task<=len(todo_list):
        remove_items=todo_list.pop(task-1)
        print(f"The {remove_items} has been removed....!!\n")
        save_tasks()
    else:
        print("Invalid choice..!!\n")

while True:
    print("To do list")
    print("1.Add the task to list")
    print("2.View the tasks")
    print("3.Remove the tasks")
    print("4.Quite")
    choice = input("Choose the options 1,2,3,4:\n")

    if choice=="1":
        task=input("Add the task \n")
        priority=input("Enter the priority has High, Medium,Low  :  ")
        todo_list.append({"task":task,"priority":priority})
        save_tasks()
        print("Task added successfully...!!!")

    elif choice=="2":
        view()

    elif choice=="3":
        view()
        task=int(input("Enter the task number to remove\n"))
        remove(task)
    elif choice=="4":
        print("Good Bye..!!")
        break
    else:
        print("invalid option selected ..!!!Please choose again")







