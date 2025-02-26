import os
import json
from datetime import datetime

#Function to format the task description string: removing double quotes and useless empty spaces
def strFormat(task_string):
        new = task_string.replace('"',' ').strip().split()
        new = " ".join(str(x) for x in new)
        return new

#Function to check if the file exists and return the correctly position to add a new task
def lines_check():
        count = 0
        try:
                f = open("tasks.json", "r")
                for x in f:
                        count+=1
                f.close()
        except:
                pass
        return count

#Function to add a new task at the bottom of the file
def add_task(desc):
        desc = strFormat(desc)
        time = datetime.now().replace(microsecond=0).strftime("%Y-%m-%d %H:%M:%S")

        count = lines_check()

        tasks_dict["id"] = count+1
        tasks_dict["description"] = desc
        tasks_dict["status"] = "Not Done"
        tasks_dict["createdAt"] = time
        tasks_dict["updatedAt"] = time

        json_task = json.dumps(tasks_dict.copy())
        f = open("tasks.json", "a")
        f.write(json_task)
        f.write("\n")
        f.close()

        x = tasks_dict.get("id")
        print(f"Task added successfully (ID: {x})")

#Function to update a task by the task id.
def update_task(task_id, new_desc):
        new_desc = strFormat(new_desc)
        time = datetime.now().replace(microsecond=0).strftime("%Y-%m-%d %H:%M:%S")


        f = open("tasks.json", "r")
        for x in f:
                tasks_list.append(json.loads(x))
        f.close()

        for x in tasks_list:
                if x["id"] == task_id:
                        x.update({"description":new_desc})
                        x.update({"updatedAt":time})
                        tasks_list[task_id-1] = x
                        break

        f = open("tasks.json", "w")
        for x in tasks_list:
                task = json.dumps(x)
                f.write(task)
                f.write("\n")
        f.close()

        tasks_list.clear()

        print(f"Task updated sucessfully (ID: {task_id})")

tasks_dict = dict()
tasks_list = list()
args = list()


while(True):
        entrada = input("task-cli ")
        
        # Clear command to clear the CLI #
        if entrada == "cls":
                os.system('cls')
        
        # ADD command to add tasks #
        if entrada.startswith("add "):
                args = entrada.split(" ", 1)
                command = args[0]

                if args[1].startswith('"') and args[1].endswith('"'):
                        task = args[1]
                        add_task(task)
                else:
                        print('Incorrect add input. Try: COMMAND "TASK_DESCRIPTION"')

        elif entrada.startswith("update "):
                args = entrada.split(" ", 2)
                command = args[0]
                if int(args[1]) and args[2].startswith('"') and args[2].endswith('"'):    
                        task_id = args[1]
                        new_desc = args[2]
                        task_id = int(task_id)
                        count = lines_check()
                        if task_id > count:
                                print(f"Task {task_id} doesn't exist")
                        
                        else:
                                update_task(task_id, new_desc)
                else:
                        print('Incorrect update command input. Try: COMMAND TASK_ID "TASK_DESCRIPTION".')
        elif entrada == "exit":
                break
        else:
                print("Incorrect Input")

        args.clear()

if os.path.exists("tasks.json"):
        os.remove("tasks.json")
else:
        print("The file does not exist")