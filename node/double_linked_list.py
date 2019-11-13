#!/usr/bin/env python3
class Node(object):
    'shuangxiang lianbiao jiedian'
    def __init__(self,item):
        self.item = item
        self.next = None
        self.prev = None

class DLinkList(object):
    'shuangxiang lianbiao'
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def get_length(self):
        cur = self._head
        count = 0
        while cur != None:
            count = count+1
            cur = cur.next
        return count

    def travel(self):
        'bianli lianbiao'
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next
        print('')

    def

