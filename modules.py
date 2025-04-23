from datetime import datetime
import json

tasks_dict = dict()
tasks_list = list()
args = list()


#Function to clear the task description, removing double quotes and white espaces
def strFormat(task_string):

        new = task_string.replace('"',' ').strip().split()
        new = " ".join(str(x) for x in new)
        return new

#Function to check if the file exists and return the number of tasks inside the file
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

#Function to set the task status to In-Progress using the ID as a reference
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

#Function to set the task status to Done using the ID as a reference
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

#Function to list all tasks created     
def listall_tasks():
        try:
                f = open("tasks.json","r")
                for x in f:
                        tasks_list.append(json.loads(x))
                f.close()

                print("ID    Status      Task")

                for x in tasks_list:
                        print(f"|{x['id']}| { x['status']} | {x['task']}")
        except:
                print("No tasks created.")
        
        tasks_list.clear()

#Function to list all tasks that are done
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

#Function to list all tasks that are no done or initiated
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

#Function to list all tasks that are in progress
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
