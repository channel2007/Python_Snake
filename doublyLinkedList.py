# encoding: utf-8
"""
#3-2-1-4
snake_body_linkedList.insert_front([1,1]) # 頭1.
snake_body_linkedList.insert_front([2,2]) # 頭2.
snake_body_linkedList.insert_front([3,3]) # 頭3.
snake_body_linkedList.insert_last([4,4])  # 尾4.

print(snake_body_linkedList.size())   # 4.
print(snake_body_linkedList.fetch(0)) # 3.
print(snake_body_linkedList.fetch(snake_body_linkedList.size()-1)) # 4.
"""

#-------------------------------------------------------------------------
# 函數:雙向串列鏈節.
# 參考:https://stonesoupprogramming.com/2017/05/20/doubly-linked-list-python/
#-------------------------------------------------------------------------
class Node:
    def __init__(self, element=None, next_node=None, prev_node=None):
        self.element = element
        self.next_node = next_node
        self.prev_node = prev_node
 
    def __str__(self):
        if self.element:
            return self.element.__str__()
        else:
            return 'Empty Node'
 
    def __repr__(self):
        return self.__str__()
 
class DoublyLinkedList:
    def __init__(self):
        self.head = Node(element='Head')
        self.tail = Node(element='Tail')
 
        self.head.next_node = self.tail
        self.tail.prev_node = self.head
 
    def size(self):
        count = 0
        current = self.head.next_node
 
        while current is not None and current != self.tail:
            count += 1
            current = current.next_node
 
        return count
 
    def insert_front(self, data):
        node = Node(element=data, next_node=self.head.next_node, prev_node=self.head)
        self.head.next_node.prev_node = node
        self.head.next_node = node
 
    def insert_last(self, data):
        node = Node(element=data, next_node=self.tail, prev_node=self.tail.prev_node)
        self.tail.prev_node.next_node = node
        self.tail.prev_node = node
 
    def insert(self, data, position):
        if position == 0:
            self.insert_front(data)
        elif position == self.size():
            self.insert_last(data)
        else:
            if 0 < position < self.size():
                current_node = self.head.next_node
                count = 0
                while count < (position - 1):
                    current_node = current_node.next_node
                    count += 1
 
                node = Node(element=data, next_node=current_node.next_node, prev_node=current_node)
                current_node.next_node.prev_node = node
                current_node.next_node = node
            else:
                raise IndexError
 
    def remove_first(self):
        self.head = self.head.next_node
        self.head.prev_node = None
 
    def remove_last(self):
        self.tail = self.tail.prev_node
        self.tail.next_node = None
 
    def remove(self, position):
        if position == 0:
            self.remove_first()
        elif position == self.size():
            self.remove_last()
        else:
            if 0 < position < self.size():
                current_node = self.head.next_node
                current_pos = 0
 
                while current_pos < position:
                    current_node = current_node.next_node
                    current_pos += 1
 
                next_node = current_node.next_node
                prev_node = current_node.prev_node
 
                next_node.prev_node = prev_node
                prev_node.next_node = next_node
            else:
                raise IndexError
 
    def fetch(self, position):
        if 0 <= position < self.size():
            current_node = self.head.next_node
            current_pos = 0
 
            while current_pos < position:
                current_node = current_node.next_node
                current_pos += 1
 
            return current_node.element
        else:
            raise IndexError