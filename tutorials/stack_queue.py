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