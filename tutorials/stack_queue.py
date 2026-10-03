#STACK: in programming paradigm where the last item added to a list is been access first (LIFO)

#QUEUE: is a method where the first item added to a list is been access first (FIFO)

class customer:
    def owner(self, owner):
        self.owner = owner


# This class is the combination of a stack and queue logic methods
class processing:

    def __init__(self):

        self.cups = []

    def add(self, cup):

        self.cups.append(cup)

    def rem_Stack(self):

        if self.is_empty():
            print("STACK CUP: is empty")
            return None
            
        return self.cups.pop() # significant difference from queue method is that it pops from the front

    def rem_Queue(self):

        if self.is_empty():
            return "Queue is empty"
        return self.cups.pop(0)

    def is_empty(self):
        return len(self.cups) == 0

    def Len(self):
        return len(self.cups)

STACK = processing()

STACK.add("Cup A")
STACK.add("Cup B")
STACK.add("Cup C")
STACK.add("Cup D")
STACK.add("Cup E")
STACK.add("Cup F")

print(STACK.Len())

for i in range(STACK.Len()):
    print(STACK.rem_Queue(), i)


## double_ended queue
## a more better way of handling a queue with the method deque


from collections import deque
import time

class TaskQueue:
    def __init__(self):
        # Initialize an empty deque
        self.queue = deque(maxlen=3)

    def add_task(self, task_name):
        """Adds a task to the end of the queue (Right side)"""
        self.queue.append(task_name)
        print(f"Added: {task_name}")

    def process_task(self):
        """Removes and processes the oldest task (Left side)"""
        if not self.queue:
            print(" No tasks left in the queue.")
            return None
        
        # O(1) performance to pop from the left
        current_task = self.queue.popleft()
        print(f"Processing: {current_task}")
        return current_task

# --- Demonstration ---
job_center = TaskQueue()

# Simulating incoming tasks
job_center.add_task("Generate PDF Report")
job_center.add_task("Send Welcome Email")
job_center.add_task("Backup Database")
job_center.add_task("CODO Database")


print(f"\nCurrent Queue Length: {len(job_center.queue)}\n")

# Processing tasks in order
job_center.process_task()
job_center.process_task()
job_center.process_task()
job_center.process_task()  # Trying to process an empty queue
