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

# function to edit previously created task
def edit_task(task_num, new_name, new_state):
    task[task_num] = new_name
    done[task_num] = new_state
    print("Task updated successfully\n")

# restructured menu to loop after each task operation and added "edit" and "exit" operations

def main():
    while True:
        print("\n=====To-Do-List=====")
        print("1.Add task")
        print("2.View tasks")
        print("3.Mark Done")
        print("4.Delete task")
        print("5.Edit task")
        print("6.Exit")

        # menu option input validation $ error handling
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        match choice:
            case 1:
                task_name = input("Enter your task name: ")
                task_state = input("Enter your task state(Done/NotDone): ").strip() #strips the whitespace to allow for better input validation
                if task_state.lower() not in ["done", "notdone"]: #change to lower so input work regardless of capitalization
                    print("Invalid state. Please enter 'Done' or 'NotDone'.")
                else:
                    add_task(task_name,task_state.upper())
                    print("Added Successfully")
            case 2:
                # check if there are any existing tasks and print message for clarity
                if not task:
                    print("No tasks available.")
                else:
                    view_tasks()

            case 3:
                # check if there are any existing tasks and print message for clarity
                if not task:
                    print("No tasks available.")
                else:
                    view_tasks()
                    # added try / except for input validation
                    try:
                        choice_done = int(input("Enter the task number to mark as done: ")) - 1
                        if 0 <= choice_done < len(task):
                            done_task(choice_done)
                        else:
                            print("Invalid task number.")
                    except ValueError:
                        print("Invalid input. Please enter a valid task number.")

            case 4:
                # check if there are any existing tasks and print message for clarity
                if not task:
                    print("No tasks available.")
                else:
                    view_tasks()
                    # added try / except for input validation
                    try:
                        choice_del = int(input("Enter the task number to delete: ")) - 1
                        if 0 <= choice_del < len(task):
                            delete_task(choice_del)
                            print("Task deleted successfully.")
                        else:
                            print("Invalid task number.")
                    except ValueError:
                        print("Invalid input. Please enter a valid task number.")

            # edit existing task
            case 5:
                if not task:
                    print("No tasks available.")
                else:
                    view_tasks()
                    try:
                        choice_edit = int(input("Enter the task number to edit: ")) - 1
                        if 0 <= choice_edit < len(task):
                            new_name = input("Enter the new task name: ")
                            new_state = input("Enter the new task state (Done/NotDone): ").strip().upper()
                            if new_state in ["DONE", "NOTDONE"]:
                                edit_task(choice_edit, new_name, new_state)
                            else:
                                print("Invalid state. Please enter 'Done' or 'NotDone'.")
                        else:
                            print("Invalid task number.")
                    except ValueError:
                        print("Invalid input. Please enter a valid task number.")

            # graceful exit via menu
            case 6:
                print("See ya next time!")
                break

            # catch all for input validation
            case _:
                print("Invalid choice. Please try again.")



if __name__ == '__main__':
        main()