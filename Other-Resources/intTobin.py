#Convert int to binary using the stack data structure

#Implementing a stack data structure using python list


class Stack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def push(self, e):
        self.data.append(e)

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.data.pop()

    def is_empty(self):
        return len(self.data) == 0


##Converter function
def intTobin(data):
    s = Stack()

    while data > 0:
        s.push(data % 2)
        data //= 2

    result = ''

    while not s.is_empty():
        result += str(s.pop())

    return result


##function in Action!!!

print(intTobin(20))
print(intTobin(14))
print(intTobin(61))
