#class for creating nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


node1 = Node(10)

#class for linking


class LinkedList:
    def __init__(self):
        #if the head is pointed to none this mean this is a empty linkedlist
        self.head = None

    #for list traversal we need to consider following things
    # if empty
    # if not empty
    def print_LL(self):
        #linkedlist traversal
        if self.head is None:
            print('Empty LinkedList')
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        #remember the return value for the new_node will be its memory address
        #point to the thing that self.head is currently pointing at
        new_node.ref = self.head
        #update the head of the linkedlist to the new node
        self.head = new_node

        ## new_node.ref , self.head = self.head , new_node


import random

k = LinkedList()
for i in [random.randint(1, 100) for _ in range(20)]:
    k.add_begin(i)
    k.print_LL()

print('Final Result')
k.print_LL()