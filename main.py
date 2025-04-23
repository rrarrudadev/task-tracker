import modules
import os

while(True):
        entrada = input("\033[1;32;40m task-cli \033[1;33;40m")
        
        # CLI CLEANING #
        if entrada == "cls":
                os.system('cls') 
        # ADD #
        elif entrada.startswith("add "):
                args = entrada.split(" ", 1)
                command = args[0]

                if args[1].startswith('"') and args[1].endswith('"'):
                        task = args[1]
                        modules.add_task(task)
                else:
                        print("\033[1;31;40m Incorrect Input")
        # UPDATE #
        elif entrada.startswith("update "):
                args = entrada.split(" ", 2)
                command = args[0]
                try:
                        if int(args[1]) and args[2].startswith('"') and args[2].endswith('"'):
                                task_id = args[1]
                                new_task = args[2]
                                task_id = int(task_id)
                                count = modules.lines_check()
                                if task_id > count:
                                        print(f"Task {task_id} doesn't exist")
                                
                                else:
                                        modules.update_task(task_id, new_task)
                        else:
                                print("\033[1;31;40m Incorrect Input")
                except:
                        print("\033[1;31;40m Incorrect Input")
        # DELETE #
        elif entrada.startswith("delete "):
                args = entrada.split(" ", 1)
                command = args[0]
                try:
                        task_id = args[1]
                        task_id = int(task_id)
                        count = modules.lines_check()
                        if task_id > count:
                                print(f"Task {task_id} doesn't exist")
                        else:
                                modules.delete_task(task_id)
                except:
                        print("\033[1;31;40m Incorrect Input")

        # MARK IN PROGRESS #
        elif entrada.startswith("mark-in-progress "):
                args = entrada.split(" ", 1)
                command = args[0]
                try:
                        task_id = args[1]
                        task_id = int(task_id)
                        count = modules.lines_check()
                        if task_id > count:
                                print(f"Task {task_id} doesn't exist")
                        else:
                                modules.mark_in_progress(task_id)
                except:
                        print("\033[1;31;40m Incorrect Input")
        # MARK DONE #
        elif entrada.startswith("mark-done "):
                args = entrada.split(" ", 1)
                command = args[0]
                try:
                        task_id = args[1]
                        task_id = int(task_id)
                        count = modules.lines_check()
                        if task_id > count:
                                print(f"Task {task_id} doesn't exist")
                        else:
                                modules.mark_done(task_id)
                except:
                        print("\033[1;31;40m Incorrect Input")

        # LISTING ALL TASKS#
        elif entrada == "list":
                modules.listall_tasks()

        #LISTING TASKS BY STATUS#
        elif entrada.startswith("list "):
                args = entrada.split(" ", 1)
                command = args[0]
                count = modules.lines_check()
                if count < 1:
                        print(f"No tasks created.")
                else:
                        if args[1] == "done":
                                modules.list_done()
                        elif args[1] == "todo":
                                modules.list_todo()
                        elif args[1] == "in-progress":
                                modules.list_inprogress()
                        else:
                                print("\033[1;31;40m Incorrect Input")
        elif entrada == "exit":
                if os.path.exists("tasks.json"):
                        os.remove("tasks.json")
                else:
                        print("The file does not exist.")
                break
        else:
                print("\033[1;31;40m Incorrect Input")

        args.clear()