import os
import json
from datetime import datetime

#Function to format the task description string: removing double quotes and useless empty spaces)
def strFormat(task_string):
        new = task_string.replace('"',' ').strip().split()
        new = " ".join(str(x) for x in new)
        return new

#Function to add a task
def add_task(desc):
        desc_clean = strFormat(desc)

        time = datetime.now().replace(microsecond=0).strftime("%Y-%m-%d %H:%M:%S")
        tasks_dict["id"] = len(tasks_list)+1
        tasks_dict["description"] = desc_clean
        tasks_dict["status"] = "Not Done"
        tasks_dict["createdAt"] = time
        tasks_dict["updatedAt"] = time
        tasks_list.append(tasks_dict.copy())

        json_task = json.dumps(tasks_dict.copy())
        f = open("tasks.json", "a")
        f.write(json_task)
        f.write("\n")
        f.close()

        x = tasks_dict.get("id")
        print(f"Task added successfully (ID: {x})")

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

                        args.clear()
                else:
                        print("Incorrect task input. You must type the task between double quotes.")
        else:
                pass
                