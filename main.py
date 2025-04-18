import json

def AddTask(tasknames, deadline):
    try:
        with open("tasks.json", "r") as file:
            taskList = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        taskList = []

    for taskname, dead in zip(tasknames, deadline):
        task = {
            'Task_Name': taskname,
            'Deadline': dead,
            'Completed': False
        }
        taskList.append(task)

    with open("tasks.json", "w") as file:
        json.dump(taskList, file, indent=4)

    
def ViewTasks():
    with open("tasks.json") as f:
        data=json.load(f)
        if not data:
            print("Sorry no tasks added yet!")
            return
        for tasks in data:
            print("Task Name : ",tasks['Task_Name'])
            print("Deadline : ",tasks['Deadline'])
            print("Completed : ",tasks['Completed'])
    return

def MarkAsCompleted(taskname):
    with open("tasks.json","r") as file:
        data=json.load(file)
        for name in taskname:
            for tasks in data:
                if tasks['Task_Name']==name:
                    tasks['Completed']=True
    with open("tasks.json","w") as f:
        json.dump(data,f)
    return

def DeleteTasks(taskname):
    with open("tasks.json","r") as file:
        data=json.load(file)
        for name in taskname:
            for tasks in data:
                if tasks["Task_Name"]==name:
                    data.remove(tasks)
    with open("tasks.json","w") as f:
        json.dump(data,f)
    return

def DelAllTasks():
    with open("tasks.json","w+") as file:
        data=[]
        json.dump(data,file)
    return

print("-------------WELCOME TO TASK MASTER---------------")
print("You have the following choices :")
print("1. Add a Task.")
print("2. View All Tasks.")
print("3. Mark Task as Completed.")
print("4. Delete Tasks (1 or more).")
print("5. Delete All Tasks.")
print("6. Exit.")
loop=True
while loop==True:
    choice=int(input("Enter Your Choice: "))
    assert(choice>=1 and choice<=6)

    if choice==1:
        tasks = input("Enter task names you want to add (comma separated): ")
        tasknames = [name.strip() for name in tasks.split(",")]
        deadline=input("Enter the deadline respectively (if any, if none write '-'): ")
        deadlines=[dead.strip() for dead in deadline.split(",")]
        AddTask(tasknames,deadlines)

    elif choice==2:
        ViewTasks()

    elif choice==3:
        tasks = input("Enter task names you completed (comma separated): ")
        tasknames = [name.strip() for name in tasks.split(",")]
        MarkAsCompleted(tasknames)
        print("All the tasks marked as completed.")

    elif choice==4:
        tasks = input("Enter task names you want to delete (comma separated): ")
        tasknames=[name.strip() for name in tasks.split(",")]
        DeleteTasks(tasknames)
        print("Tasks Deleted succesfully")

    elif choice==5:
        DelAllTasks()
        print("All Tasks Deleted.")

    elif choice==6:
        print("See ya Soon! Bye Bye")
        loop=False


