#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep):
    print()
    while node:
        print(str(node.data), end="")

        node = node.next

        if node:
            print(sep, end="")

    print()
    print()


def deleteNode(head, position):

    # no need to change next pointers if head is deleted
    if position == 0:
        return head.next
    
    prevNode = head
    for _ in range(1, position):
        prevNode = prevNode.next

    # skip out delete node
    prevNode.next = prevNode.next.next
    return head

if __name__ == '__main__':

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input())

    llist1 = deleteNode(llist.head, position)

    print_singly_linked_list(llist1, ' ')
    # print()