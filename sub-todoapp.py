def main():
    tasks = []
    
    while True:
        print("\n ------ To-Do List -----")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Mark task as done")
        print("4. Exit")
        
        choice = input("Enter your choice:")
        
        if choice == "1":
            print()
            n_tasks = int(input("How many task do you want to add: "))
            
            for i in range(n_tasks):
                task = input("Enter the task:")
                if task not in [t["task"] for t in tasks]:
                  tasks.append({"task": task, "done": False})
                  print("Task added!")
                else:
                    print("Task already exists")
        
        elif choice == "2":
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task["task"]} - {status}")
                
        elif choice == "3":
            task_index = int(input("Enter the task number to mark as done:"))
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number")
          
        elif choice == "4":
            print("Exiting the To-do list")
            break
        else:
            print("Invalid choice.Please try again")
            
if __name__ == "__main__":
    main()
