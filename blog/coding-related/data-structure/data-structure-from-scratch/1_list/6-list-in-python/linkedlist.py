
class LinkedList(object):

    class __Node(object):
        def __init__(self, item):
            self.item = item
            self.next = None

    def __init__(self):
        self.__head = self.__Node(None)
        self.__head.next = None
        self.__length = 0

    def insert(self, index, value):
        if index > self.__length+1 or index < 1:
            raise IndexError

        node = self.__Node(value)
        if self.__length == 0:  # index == 1
            self.__head.next = node
            self.__length += 1
            return True

        p = self.__head
        for i in range(index-1):
            p = p.next

        node.next = p.next
        p.next = node
        self.__length += 1
        return True

    def print_list(self):
        p = self.__head
        count = 0
        while p.next is not None and count <= self.__length:
            p = p.next
            if count != 0 and count % 10 == 0:
                print()
            print(p.item, end=' ')
            count += 1
        print()

    def remove(self, index):
        if index > self.__length or index < 1:
            raise IndexError
        p = self.__head
        for i in range(index - 1):
            p = p.next
        p.next = p.next.next
        return True

    def replace(self, index, value):
        if index > self.__length or index < 1:
            raise IndexError
        p = self.__head
        for i in range(index):
            p = p.next
        p.item = value
        return True

    def get(self, index):
        if index > self.__length or index < 1:
            raise IndexError
        p = self.__head
        for i in range(index):
            p = p.next
        return p.item

    def find(self, value):
        p = self.__head
        count = 0
        while p.next is not None:
            p = p.next
            count += 1
            if p.item is value:
                return count
        return -1

    def length(self):
        return self.__length


if __name__ == '__main__':
    li = LinkedList()
    for i in range(20):
        li.insert(i+1, i+1)
        # print(i)
    li.print_list()
    li.insert(21, 999)

    # li.insert(50, 8989879)
    li.print_list()
    li.remove(21)
    li.print_list()
    li.replace(10, 77)
    li.print_list()
    print(li.get(10))
    print(li.find(77))
    print(li.length())

    print('='*30)

    s_li = LinkedList()
    for i in range(20):
        s_li.insert(i+1, '*')
    s_li.print_list()
    s_li.insert(10, '&')
    s_li.insert(15, '$')
    s_li.print_list()
    s_li.replace(22, '@')
    s_li.print_list()
    s_li.remove(22)
    s_li.print_list()
    print(s_li.find('&'))
    print(s_li.get(10))
    print(s_li.length())

"""results
1 2 3 4 5 6 7 8 9 10 
11 12 13 14 15 16 17 18 19 20 
1 2 3 4 5 6 7 8 9 10 
11 12 13 14 15 16 17 18 19 20 
999 
1 2 3 4 5 6 7 8 9 10 
11 12 13 14 15 16 17 18 19 20 
1 2 3 4 5 6 7 8 9 77 
11 12 13 14 15 16 17 18 19 20 
77
10
21
==============================
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * & 
* * * * $ * * * * * 
* * 
* * * * * * * * * & 
* * * * $ * * * * * 
* @ 
* * * * * * * * * & 
* * * * $ * * * * * 
* 
10
&
22

Process finished with exit code 0
"""

