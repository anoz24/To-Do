task = []
done = []
def add_task(name , state):
    task.append(name)
    done.append(state)
def view_tasks():
    if len(task) == len(done):
        for i in range(0,len(task),1):
            print(f"Task {i+1} ==> Name:{task[i]} , State:{done[i]}\n")
def delete_task(task_num):
    task.pop(task_num)
    done.pop(task_num)
def done_task(task_num):
    if done[task_num] == "DONE":
        print("Task already done\n")
    else:
        done[task_num] = "DONE"
        print("Task marked done successfully\n")
def main():
    print("1.Add task")
    print("2.View tasks")
    print("3.Mark Done")
    print("4.Delete task")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            task_name = input("Enter your task name: ")
            task_state = input("Enter your task state(Done/NotDone): ")
            add_task(task_name,task_state.upper())
            print("Added Successfully")
        case 2:
            view_tasks()
        case 3:
            view_tasks()
            choice_done = int(input("Enter your choice to mark as done:"))
            done_task(choice_done-1)
        case 4:
            view_tasks()
            choice_del = int(input("Enter your choice to delete:"))
            delete_task(choice_del-1)
            print("Deleted Successfully")
        case default:
            print("Invalid Choice")



if __name__ == '__main__':
    print("=====To-Do-List=====")
    while True:
        main()