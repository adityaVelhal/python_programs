COUNT = 0


class CircularLinkedList:

    def __init__(self):
        self.start = None

    def display(self):
        if COUNT == 0:
            print("\nList is empty\n")
        else:
            tmp = self.start
            data_list = []
            for i in range(COUNT):
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
            self.start.next = self.start
        elif COUNT == 1:
            new_node.next = self.start
            self.start.next = new_node
            self.start = new_node

        else:
            new_node.next = self.start
            self.start = new_node

            tmp = self.start
            for i in range(COUNT):
                tmp = tmp.next

            tmp.next = self.start
        COUNT += 1

    def insert_at_end(self, val):
        global COUNT
        new_node = Node(val)
        new_node.next = self.start

        if self.start is None:
            self.start = new_node
        else:
            tmp = self.start

            for i in range(COUNT - 1):
                tmp = tmp.next

            tmp.next = new_node

        COUNT += 1

    def insert_in_between(self, val, pos):
        global COUNT

        if pos > COUNT:
            print("\nPosition not available.\n")
        elif pos == COUNT:
            self.insert_at_end(val)
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
                ptr = self.start

                for i in range(COUNT - 1):
                    ptr = ptr.next

                ptr.next = self.start

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
                for i in range(COUNT - 1):
                    ptr = tmp
                    tmp = tmp.next

                ptr.next = tmp.next

            print("\n{} deleted.\n".format(tmp.data))
            del tmp
            COUNT -= 1

    def delete_in_between(self, pos):
        global COUNT

        if pos > COUNT:
            print("\nPosition does not exist.\n")
        elif pos == COUNT:
            self.delete_end()
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
    CLL = CircularLinkedList()

    while True:
        ch = int(input("1.Insert\n2.Delete\n3.Display\n4.Exit\nEnter choice : "))
        if ch == 1:
            ch = int(input("\n1.At beginning\n2.At End\n3.In between\nEnter choice : "))
            val = int(input("\nEnter value : "))

            if ch == 1:
                CLL.insert_at_beginning(val)
            elif ch == 2:
                CLL.insert_at_end(val)
            elif ch == 3:
                pos = int(input("Enter position : "))
                CLL.insert_in_between(val, pos)
            else:
                print("\nEnter correct choice.\n")

        elif ch == 2:
            ch = int(input("\n1.At beginning\n2.At End\n3.In between\nEnter choice : "))

            if ch == 1:
                CLL.delete_beginning()
            elif ch == 2:
                CLL.delete_end()
            elif ch == 3:
                pos = int(input("Enter position : "))
                CLL.delete_in_between(pos)
            else:
                print("\nEnter correct choice.\n")

        elif ch == 3:
            CLL.display()

        elif ch == 4:
            break

        else:
            print("\nEnter correct choice.\n")
