class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, *args):
        self.head = None
        self.tail = None
        self.length = 0
        if args:
            for arg in args:
                self.append(arg)

    def add_forward(self, el):
        new_node = Node(el)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def append(self, el):
        new_node = Node(el)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self, index=0):
        if index < 0 or index >= self.length:
            raise IndexError('pop index out of range')
        if index == 0:
            value = self.head.head
            self.head = self.head.next
            if not self.head:
                self.tail = None
        else:
            curr_node = self.head
            for _ in range(index - 1):
                curr_node = curr_node.next
            value = curr_node.next.head
            if curr_node.next is self.tail:
                self.tail = curr_node
            curr_node.next = curr_node.next.next
        self.length -= 1
        return value

    def __add__(self, other):
        if not isinstance(other, LinkedList):
            raise TypeError(f'can only concatenate LinkedList (not "{type(other).__name__}") to LinkedList')
        new_linked_list = LinkedList()
        curr_node = self.head
        while curr_node:
            new_linked_list.append(curr_node.head)
            curr_node = curr_node.next
        curr_node = other.head
        while curr_node:
            new_linked_list.append(curr_node.head)
            curr_node = curr_node.next
        return new_linked_list

    def __getitem__(self, index):
        if index < 0 or index >= self.length:
            raise IndexError('list index out of range')
        curr_node = self.head
        for _ in range(index):
            curr_node = curr_node.next
        return curr_node.head

    def __setitem__(self, index, value):
        if index < 0 or index >= self.length:
            raise IndexError('list index out of range')
        curr_node = self.head
        for _ in range(index):
            curr_node = curr_node.next
        curr_node.head = value

    def __len__(self):
        return self.length

    def __str__(self):
        nodes = []
        curr_node = self.head
        while curr_node:
            nodes.append(str(curr_node.head))
            curr_node = curr_node.next
        return '(' + ' -> '.join(nodes) + ')'
    
    def __repr__(self):
        nodes = []
        curr_node = self.head
        while curr_node:
            nodes.append(str(curr_node.head))
            curr_node = curr_node.next
        wtf='LinkedList'+'(' + ', '.join(nodes) + ')'
        return wtf
    def remove(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

def remove(link_list, k):
    '''
    Учитывая связанный список, меняет местами k-ый элемент с самого начала с k-ым элементом с конца.  
    >>> l1 = LinkedList(1,2,3,4,5)
    >>> remove(l1, 2)
    >>> l1
    (1 -> 4 -> 3 -> 2 -> 5)
    '''
    if k < 0 or k >= len(link_list):
        raise IndexError('Index out of range')

    if k == 0 or k == len(link_list) - 1:
        return link_list

    # Находим k-ый элемент с начала
    first_element = link_list[k]

    # Находим k-ый элемент с конца
    last_element = link_list[len(link_list) - k - 1]

    # Меняем значения местами
    link_list[k] = last_element
    link_list[len(link_list) - k - 1] = first_element

    return link_list

def alternating_split(link_list):
    if len(link_list) == 0:
        return None, None
    
    if len(link_list) == 1:
        return link_list, None
    
    # Создаем два новых списка
    list1 = LinkedList()
    list2 = LinkedList()
    
    # Чередуем элементы из исходного списка
    for i in range(len(link_list)):
        if i % 2 == 0:
            list1.append(link_list[i])
        else:
            list2.append(link_list[i])
    
    return list1, list2
