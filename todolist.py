
#the scope of this project is to create the --todo list with the add,remove,view functionalities
todo_list=[]

def add(task):
    todo_list.append(task)
    print(f"the {task} has been added to the list..!!")

def view():
    if not todo_list:
        print("No task to show")
    else:
        print("Here are the tasks..!!!")
        for x,task in enumerate(todo_list,start=1):
            print(f"{x}--{task}")


def remove(task):
    if task<=len(todo_list):
        remove_items=todo_list.pop(task-1)
        print(f"The {remove_items} has been removed....!!\n")
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
        add(task)
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







