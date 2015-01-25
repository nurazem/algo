from random import randint

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self,value):
        node = Node(value)
        #if the old list is none, set new node as the first node
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def __str__(self):
        if self.head != None:
            index = self.head
            nodestore = [str(index.value)]
            while index.next != None:
                index = index.next
                nodestore.append(str(index.value))
            return "LinkedList  [ " + "->".join(nodestore) + " ]"
        return "LinkedList  []"

def randomLinkedList(length, min, max):
    linkedlist = LinkedList()
    for i in range(length):
        value = randint(min, max)
        linkedlist.addNode(value)
    return linkedlist

def partition_list(linked_list, x):
    before = LinkedList()
    after = LinkedList()
    pointer = linked_list.head
    while pointer is not None:
        if pointer.value >= x:
            after.addNode(pointer.value)
        else:
            before.addNode(pointer.value)
        pointer = pointer.next

    before.tail.next = after.head
    return before


ll = randomLinkedList(10, 1, 10)
print ll
print partition_list(ll, 5)
