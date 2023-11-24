class Node:
    def __init__(self, info):
        self.info = info
        self.next = None


class Task:
    task_count = 0

    def __init__(self, description, priority):
        Task.task_count += 1
        self.task_id = Task.task_count
        self.description = description
        self.priority = priority
        self.completed = False

    def get_Taskid(self):
        return self.task_id

    def get_Description(self):
        return self.description

    def set_Description(self, description):
        self.description = description

    def get_Priority(self):
        return self.priority

    def set_Priority(self, priority):
        self._priority = priority

    def is_Completed(self):
        return self.completed

    def set_Completed(self, completed):
        self.completed = completed


class PriorityQueue:
    def __init__(self):
        self.header = None # reference to the first nod in quque
        self.size = 0  # track size of quque

    def display_Queue(self):
        current = self.header # refernce to the fist item in quque

        while current.next is not None: #looping around nod to print all items
            print(current.info, end="--") # each time a current info is printed its ends by --
            current = current.next

        print(current.info)

    def enqueue(self, info):
        node = Node(info)

        if self.size == 0: # if quque is empty the the first node will be added to the head
            self.header = node
            self.size += 1
            print( node.info," has been added")

        else:# else if the ndoe is greater then the header it will compare itsdelf to the next node to find its right place
            if node.info > self.header.info: 
                node.next = self.header
                self.header = node
                self.size += 1

            else:
                current = self.header
                previous = current

                while current is not None and current.info >= node.info:
                    previous = current
                    current = current.next

                previous.next = node
                node.next = current
                self.size += 1

    def dequeue(self):
        if self.size == 0:
            print(" Queue is Empty.")
        elif self.size == 1:
            print("removing:", self.header.info)
            self.header = None
            self.size -= 1
        else:
            print("removing:", self.header.info)
            current = self.header
            self.header = self.header.next
            current.next = None
            self.size -= 1


class Stack:
    def __init__(self):
        self.header = None
        self.size = 0

    def isEmpty(self):
        return self.header is None # check if stack empty 

    def displayStack(self):
        current = self.header

        while current is not None: #  display whats in stack 
            print("|" + str(current.info) + "|")
            current = current.next

        print("---")

    def push(self, info):
        node_to_add = Node(info)

        node_to_add.next = self.header
        self.header = node_to_add
        self.size += 1

    def pop(self):
        if self.isEmpty():
            print("empty stack.")
        else:
            temp = self.header
            self.header = self.header.next
            temp.next = None
            self.size -= 1
            return temp.info

    def peek(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            print("The top of stack is :", self.header.info)


task1 = Task("Complete assignment", 2)
task2 = Task("Read a book", 1)
task3 = Task("Write report", 3)

priority_queue = PriorityQueue()


priority_queue.enqueue(task1.get_Priority())
priority_queue.enqueue(task2.get_Priority())
priority_queue.enqueue(task3.get_Priority())


priority_queue.display_Queue()


priority_queue.dequeue()
priority_queue.display_Queue()

completed_stack = Stack()


completed_stack.push(task1.get_Taskid())
completed_stack.push(task2.get_Taskid())
completed_stack.push(task3.get_Taskid())


completed_stack.displayStack()


completed_stack.pop()
completed_stack.displayStack()



class TaskManager:
    def __init__(self):
        self.task_queue = PriorityQueue()
        self.task_history = Stack()

    def add_task(self, description, priority):
        task = Task(description, priority)
        self.task_queue.enqueue(task)
        print("Task added successfully.")

    def get_task(self, task_id):
        
        pass

    def complete_highest_priority_task(self):
        task = self.task_queue.dequeue()
        if task:
            task.set_completed(True)
            self.task_history.push(task)
            print("Task completed and moved to history.")
        else:
            print("No tasks in the queue.")

    def display_all_tasks(self):
      if self.task_queue.size == 0:
          print("No tasks in the queue.")
      else:
          print("All tasks in order of priority:")
          self.task_queue.display_Queue()

    def display_incomplete_tasks(self):
      if self.task_queue.size == 0:
          print("No tasks in the queue.")
      else:
          print("Incomplete tasks:")
          current = self.task_queue.header
          while current is not None:
            task = current.info
            if not task.is_completed():
                print(f"Task ID: {task.get_task_id()}, Description: {task.get_description()}, Priority: {task.get_priority()}, Completed: {task.is_completed()}")
            current = current.next

    def display_last_completed_task(self):
        last_completed_task = self.task_history.peek()
        if last_completed_task:
            print("Last completed task:", last_completed_task.get_description())
        else:
            print("No completed tasks in history.")
    
    def display_menu(self):
        while True:
            print("\nTask Manager Menu:")
            print("1. Add a new task")
            print("2. Get a task by ID")
            print("3. Complete the highest priority task")
            print("4. Display all tasks in order of priority")
            print("5. Display only incomplete tasks")
            print("6. Display the last completed task")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                description = input("Enter task description: ")
                priority = int(input("Enter task priority: "))
                self.add_task(description, priority)
            elif choice == "2":
                task_id = int(input("Enter task ID: "))
                self.get_task(task_id)
            elif choice == "3":
                self.complete_highest_priority_task()
            elif choice == "4":
                self.display_all_tasks()
            elif choice == "5":
                self.display_incomplete_tasks()
            elif choice == "6":
                self.display_last_completed_task()
            elif choice == "7":
                print("Exiting")
                exit()
            else:
                print("Invalid choice. Please enter a valid option.")


task_manager = TaskManager()

task_manager.display_menu()
