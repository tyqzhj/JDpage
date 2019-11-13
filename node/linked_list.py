#!/usr/bin/env python3
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self,head=None):
        self.head = head

    def append(self,new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def is_empty(self):
        return not self.head

    def get_length(self):
        temp = sel.head
        length = 0
        while temp != None:
            length = length+1
            temp = temp.next
        return length

    def insert(self,position,new_element):
        '''
        zai lianbao zhiding suoyinchu charu yuansu
        '''
        if position < 0 or position > self.get_length():
            raise IndexError('insert position outside range.')
        temp = self.head
        if position == 0:
            new_element.next,self.head = temp,new_element
            return
        i = 0
        'bianli zhaodao suoyinzhi position jiedianhou, zai qihoumian charu jiedian'
        while i < position:
            pre,temp = temp,temp.next
            i += 1
        pre.next,new_element.next = new_element,temp

    def print_list(self):
        '''
        bianli lianbiao, bing yici dayin yuansu
        '''
        print('linked_list:')
        temp = self.head
        new_list = []
        while temp is not None:
            new_list.append(temp.data)
            temp = temp.next
        print(new_list)

    def remove(self,position):
        '''
        shanchu zhiding suoyin de lianbiao yuansu
        '''
        if position < 0 or position > self.get_length():
            raise IndexError('remove position outside range.')
        temp = self.head
        i = 0
        'bianli zhaodao suoyinzhi position de jiedian'
        while temp != None:
            if position == 0:
                self.head = temp.next
                temp.next = None
                return True
            pre,temp = temp,temp.next
        i += 1
        if i == position:
            pre.next,temp.next = temp.next,None
            return

    def reverse(self):
        'jiang lianbiao fanzhuan'
        prev = None
        current = self.head
        while current:
            next_node,current.next = current.next,prev
            prev,current = current,next_node
        self.head = prev

    def initlist(self,data_list):
        'jiang liebiao zhuanhuancheng lianbiao'
        'chaungjian tou jiedian'
        self.head = Node(data_list[0])
        temp = self.head
        'zhuge wei data shuju chuangjian jiedian jianli lianbiao'
        for i in data_list[1:]:
            node = Node(i)
            temp.next = node
            temp = temp.next
