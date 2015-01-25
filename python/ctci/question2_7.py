from random import randint

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        result = ""
        node = self
        while node is not None:
            result += "({0})->".format(node.value)
            node = node.next
        return result

def remove_tail(head):
    while head.next.next is not None:
        head = head.next
    tail = head.next
    head.next = None
    return tail

def is_palindrome(head):
    if head is None or head.next is None:
        return True
    tail = remove_tail(head)
    print tail.value
    print head.value
    if head.value == tail.value:
        head = head.next
    else:
        return False
    print head
    return is_palindrome(head)


n = Node(10)
n.next = Node(20)
n.next.next = Node(40)
n.next.next.next = Node(30)
n.next.next.next.next = Node(30)
n.next.next.next.next.next = Node(20)
n.next.next.next.next.next.next = Node(10)

print n
print is_palindrome(n)
