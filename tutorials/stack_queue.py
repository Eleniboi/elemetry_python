#STACK: in programming paradigm where the last item added to a list is been access first (LIFO)

#QUEUE: is a method where the first item added to a list is been access first (FIFO)

class customer:
    def owner(self, owner):
        self.owner = owner


class processing:

    def __init__(self):

        self.cups = []

    def add(self, cup):

        self.cups.append(cup)

    def rem(self):

        if self.is_empty():
            print("STACK CUP: is empty")
            return None
            
        return self.cups.pop()

    def is_empty(self):
        return len(self.cups) == 0

STACK = processing()

STACK.add("Cup A")
STACK.add("Cup B")

print(STACK.rem())
print(STACK.rem())
print(STACK.rem())