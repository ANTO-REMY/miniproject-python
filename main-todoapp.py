tasks = []


def add_task():
    task = input("Please enter a task:")
    tasks.append(task)
    print("Task {tasks} added to the list")


def list_task():
    if not tasks:
        print("There are no tasks currently")
    else:
        print("Currently tasks:")
        for index, task in enumerate(tasks):
            print(f"Task{index+1}. {tasks} ")


def delete_task():
    list_task()
    try:
        task_to_delete = int(input("Enter the no to delete: "))
        if task_to_delete < len(tasks):
            tasks.pop(task_to_delete)
            print(f"Task {task_to_delete} has been removed")
        else:
            print(f"Task {task_to_delete} was not found")
    except:
        print("Invalid input.")


if __name__ == "__main__":
    #create a loop to run the app
    print("Welcome to the to do list app😁")
    while True:
        print('\n')
        print('Please select one of the following:')
        print('-------------------------------------')
        print('1. Add tasks')
        print('2. Delete a task')
        print('3. List tasks')
        print('4. Quit')

        choice = input("Enter your choice:")
        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            list_task()
        elif choice == "4":
            break
        else:
            print("Invalid input. Please try again")

print("\n")
print("Goodbye🫡")
