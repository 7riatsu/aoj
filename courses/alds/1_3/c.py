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
            if node.val == value: # TODO: ここの `==` と `is` の使い分けを調べる
                if node.prev is None and node.next is None:
                    self.head = self.tail = None
                else:
                    if node.prev is not None:
                        node.prev.next = node.next
                    else:
                        self.head = self.head.next
                    if node.next is not None:
                        node.next.prev = node.prev
                    else:
                        self.tail = self.tail.prev
                break
            node = node.next

    def delete_first(self):
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next

    def delete_last(self):
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev

    def get_elements(self):
        ele = self.head
        elms = []

        while ele is not None:
            elms.append(ele.val)
            ele = ele.next
        return " ".join(elms)

def _main():
    from sys import stdin

    n = int(input())

    lst = DoublyLinkedList()

    for _ in range(n):
        cmd = stdin.readline().strip().split()
        if cmd[0] == 'insert':
            lst.insert(cmd[1])
        elif cmd[0] == 'delete':
            lst.delete(cmd[1])
        elif cmd[0] == 'deleteFirst':
            lst.delete_first()
        elif cmd[0] == 'deleteLast':
            lst.delete_last()

    print(lst.get_elements())

if __name__ == '__main__':
    _main()
