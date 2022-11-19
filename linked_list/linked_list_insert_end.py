
class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, value):
        if self.head is None:
            self.head = Node(value, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(value, itr.next)
        itr.next = node
        return

    def print_linked_list(self):
        itr = self.head
        lst = []
        while itr:
            lst.append(itr.data)
            itr = itr.next

        print(" -> ".join(lst))
        return


if __name__ == '__main__':
    input_string = input('Enter elements separated by space \n')
    user_list = input_string.split()
    print('Input list: ', user_list)
    ll = LinkedList()
    for i in user_list:
        ll.insert_end(i)
    ll.print_linked_list()

