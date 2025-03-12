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
        tasks_dict["task"] = desc
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
def update_task(task_id, new_task):

        new_task = strFormat(new_task)
        time = datetime.now().replace(microsecond=0).strftime("%Y-%m-%d %H:%M:%S")


        f = open("tasks.json", "r")
        for x in f:
                tasks_list.append(json.loads(x))
        f.close()

        for x in tasks_list:
                if x["id"] == task_id:
                        x.update({"task":new_task})
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

#Function to delete a task by the task id.
def delete_task(task_id):

        f = open("tasks.json", "r")
        for x in f:
                tasks_list.append(json.loads(x))
        f.close()

        for x in tasks_list:
                if x["id"] == task_id:
                        tasks_list.remove(x)
        
        cont = 1

        for x in tasks_list:
                x["id"] = cont
                cont+=1

        f = open("tasks.json", "w")
        for x in tasks_list:
                task = json.dumps(x)
                f.write(task)
                f.write("\n")
        f.close()

        tasks_list.clear()
        print(f"Task {task_id} deleted")

def mark_in_progress(task_id):

        f = open("tasks.json", "r")
        for x in f:
                tasks_list.append(json.loads(x))
        f.close()

        for x in tasks_list:
                if x["id"] == task_id:
                        x.update({"status":"In Progress"})
                        tasks_list[task_id-1] = x
                        break

        f = open("tasks.json", "w")
        for x in tasks_list:
                task = json.dumps(x)
                f.write(task)
                f.write("\n")
        f.close()

        tasks_list.clear()

def mark_done(task_id):

        f = open("tasks.json", "r")
        for x in f:
                tasks_list.append(json.loads(x))
        f.close()

        for x in tasks_list:
                if x["id"] == task_id:
                        x.update({"status":"Done"})
                        tasks_list[task_id-1] = x
                        break

        f = open("tasks.json", "w")
        for x in tasks_list:
                task = json.dumps(x)
                f.write(task)
                f.write("\n")
        f.close()

        tasks_list.clear()
        
def listall_tasks():
        f = open("tasks.json","r")
        for x in f:
                tasks_list.append(json.loads(x))
        f.close()
        
        print("ID    Status      Task")

        for x in tasks_list:
                print(f"|{x['id']}| { x['status']} | {x['task']}")

        tasks_list.clear()

def list_done():
        f = open("tasks.json","r")
        for x in f:
                tasks_list.append(json.loads(x))
        f.close()
        
        print("ID    Status      Task")

        for x in tasks_list:
                if x["status"] == "Done":
                        print(f"|{x['id']}| { x['status']} | {x['task']}")

        tasks_list.clear()

def list_todo():
        f = open("tasks.json","r")
        for x in f:
                tasks_list.append(json.loads(x))
        f.close()
        
        print("ID    Status      Task")

        for x in tasks_list:
                if x["status"] == "Not Done":
                        print(f"|{x['id']}| { x['status']} | {x['task']}")

        tasks_list.clear()

def list_inprogress():
        f = open("tasks.json","r")
        for x in f:
                tasks_list.append(json.loads(x))
        f.close()
        
        print("ID    Status      Task")

        for x in tasks_list:
                if x["status"] == "In Progress":
                        print(f"|{x['id']}| { x['status']} | {x['task']}")

        tasks_list.clear()


tasks_dict = dict()
tasks_list = list()
args = list()


while(True):
        entrada = input("task-cli ")
        
        # Clear command to clear the CLI #
        if entrada == "cls":
                os.system('cls')
        
        # ADD #
        if entrada.startswith("add "):
                args = entrada.split(" ", 1)
                command = args[0]

                if args[1].startswith('"') and args[1].endswith('"'):
                        task = args[1]
                        add_task(task)
                else:
                        print('Incorrect add input. Try: COMMAND "TASK_DESCRIPTION"')
        # UPDATE #
        elif entrada.startswith("update "):
                args = entrada.split(" ", 2)
                command = args[0]
                if int(args[1]) and args[2].startswith('"') and args[2].endswith('"'):    
                        task_id = args[1]
                        new_task = args[2]
                        task_id = int(task_id)
                        count = lines_check()
                        if task_id > count:
                                print(f"Task {task_id} doesn't exist")
                        
                        else:
                                update_task(task_id, new_task)
                else:
                        print('Incorrect update command input. Try: COMMAND TASK_ID "TASK_DESCRIPTION".')
        # DELETE #
        elif entrada.startswith("delete "):
                args = entrada.split(" ", 1)
                command = args[0]
                if int(args[1]):
                        task_id = args[1]
                        task_id = int(task_id)
                        count = lines_check()
                        if task_id > count:
                                print(f"Task {task_id} doesn't exist")
                        else:
                                delete_task(task_id)
        # MARK IN PROGRESS #
        elif entrada.startswith("mark-in-progress "):
                args = entrada.split(" ", 1)
                command = args[0]
                if int(args[1]):
                        task_id = args[1]
                        task_id = int(task_id)
                        count = lines_check()
                        if task_id > count:
                                print(f"Task {task_id} doesn't exist")
                        else:
                                mark_in_progress(task_id)
        # MARK DONE #                                
        elif entrada.startswith("mark-done "):
                args = entrada.split(" ", 1)
                command = args[0]
                if int(args[1]):
                        task_id = args[1]
                        task_id = int(task_id)
                        count = lines_check()
                        if task_id > count:
                                print(f"Task {task_id} doesn't exist")
                        else:
                                mark_done(task_id)

        # LISTING ALL TASKS#
        elif entrada == "list":
                listall_tasks()

        #LISTING TASKS BY STATUS#
        elif entrada.startswith("list "):
                args = entrada.split(" ", 1)
                command = args[0]
                if args[1] == "done":
                        list_done()
                elif args[1] == "todo":
                        list_todo()
                elif args[1] == "in-progress":
                        list_inprogress()
        elif entrada == "exit":
                break
        else:
                print("Incorrect Input")

        args.clear()

if os.path.exists("tasks.json"):
        os.remove("tasks.json")
else:
        print("The file does not exist")