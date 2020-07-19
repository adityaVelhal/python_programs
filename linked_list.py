COUNT = 0


class LinkedList:

    def __init__(self):
        self.start = None

    def display(self):
        tmp = self.start
        data_list = []
        while tmp is not None:
            data_list.append(tmp.data)
            tmp = tmp.next
        print()
        print(*data_list, sep=" --> ")
        print()

    def insert_at_beginning(self, val):
        global COUNT
        new_node = Node(val)

        if self.start is None:
            self.start = new_node
        else:
            new_node.next = self.start
            self.start = new_node

        COUNT += 1

    def insert_at_end(self, val):
        global COUNT
        new_node = Node(val)

        if self.start is None:
            self.start = new_node
        else:
            tmp = self.start

            while tmp.next is not None:
                tmp = tmp.next

            tmp.next = new_node

        COUNT += 1

    def insert_in_between(self, val, pos):
        global COUNT

        if pos > COUNT:
            print("Position not available.")
        else:
            if pos == 1:
                self.insert_at_beginning(val)
            else:
                new_node = Node(val)
                tmp = self.start
                ptr = Node(None)
                for i in range(1, pos):
                    ptr = tmp
                    tmp = tmp.next
                new_node.next = tmp
                ptr.next = new_node

            COUNT += 1

    def delete_beginning(self):
        global COUNT

        if self.start is None:
            print("\nList is empty\n")
        else:
            tmp = self.start
            if COUNT == 1:
                self.start = None
            else:
                self.start = tmp.next

            print("\n{} deleted.\n".format(tmp.data))
            del tmp
            COUNT -= 1

    def delete_end(self):
        global COUNT

        if self.start is None:
            print("\nList is empty\n")
        else:
            tmp = self.start

            if COUNT == 1:
                self.start = None
            else:
                ptr = Node(None)
                while tmp.next is not None:
                    ptr = tmp
                    tmp = tmp.next

                ptr.next = None

            print("\n{} deleted.\n".format(tmp.data))
            del tmp
            COUNT -= 1

    def delete_in_between(self, pos):
        global COUNT

        if pos > COUNT:
            print("\nPosition does not exist.\n")
        else:
            if pos == 1:
                self.delete_beginning()
            elif pos == COUNT:
                self.delete_end()
            else:
                tmp = self.start
                ptr = Node(None)

                for i in range(1, pos):
                    ptr = tmp
                    tmp = tmp.next

                ptr.next = tmp.next
                print("\n{} deleted.\n".format(tmp.data))
                del tmp
                COUNT -= 1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":

    ll = LinkedList()

    while True:
        ch = int(input("1.Insert\n2.Delete\n3.Display\n4.Exit\nEnter choice : "))
        if ch == 1:
            ch = int(input("\n1.At beginning\n2.At End\n3.In between\nEnter choice : "))
            val = int(input("\nEnter value : "))

            if ch == 1:
                ll.insert_at_beginning(val)
            elif ch == 2:
                ll.insert_at_end(val)
            elif ch == 3:
                pos = int(input("Enter position : "))
                ll.insert_in_between(val, pos)
            else:
                print("\nEnter correct choice.\n")

        elif ch == 2:
            ch = int(input("\n1.At beginning\n2.At End\n3.In between\nEnter choice : "))

            if ch == 1:
                ll.delete_beginning()
            elif ch == 2:
                ll.delete_end()
            elif ch == 3:
                pos = int(input("Enter position : "))
                ll.delete_in_between(pos)
            else:
                print("\nEnter correct choice.\n")

        elif ch == 3:
            ll.display()

        elif ch == 4:
            break

        else:
            print("\nEnter correct choice.\n")
