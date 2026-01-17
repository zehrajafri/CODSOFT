def to_do_list():
    tasks = []

    while True:
        print("1. Add task")
        print("2. Remove task")
        print("3. Show tasks")
        print("4.Quit")
        choice = input("Ënter preffered choice:")

        if choice == "1":
            task = input("Enter required tasks to do: ")
            tasks.append(task)
        elif choice == "2":
             task = input("Enter tasks to be removed: ")
             if task in tasks:
                 tasks.remove(task)
             else:
                  print("Task not found")
        elif choice == "3":
            print("Tasks: ")
            for task in tasks:
                print("- " + task)
        elif choice == "4":
            break
        else:
            print("Invalid choice")
to_do_list()
           
        
            
            
            
    
