class Node:
    def __init__(self, value):
        self.prev = None
        self.val = value
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, value):
        node = self.head

        while node is not None:
            if node.val == value:
                if node.prev == None and node.next == None:
                    self.head = self.tail = None
                else:
                    if node.prev != None:
                        node.prev.next = node.next
                    else:
                        self.head = self.head.next
                    if node.next != None:
                        node.next.prev = node.prev
                    else:
                        self.tail = self.tail.prev
                break
            node = node.next

    def delete_first(self):
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next

    def delete_last(self):
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev

    def show_value(self):
        ele = self.head
        elms = []

        while ele is not None:
            elms.append(ele.val)
            ele = ele.next
        print(*elms)

l = DoublyLinkedList()

n = int(input())

for _ in range(n):
    command = input().strip().split()
    if command[0] == "insert":
        l.insert(command[1])
    elif command[0] == "delete":
        l.delete(command[1])
    elif command[0] == "deleteFirst":
        l.delete_first()
    elif command[0] == "deleteLast":
        l.delete_last()
    else:
        pass

l.show_value()
