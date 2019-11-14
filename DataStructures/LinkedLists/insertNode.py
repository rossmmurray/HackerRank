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

def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data))
        node = node.next

        if node:
            print(sep)

def addNode(node, data):
    if node.next:
        addNode(node.next, data)
    else:
        node.next = SinglyLinkedListNode(data)

def insertNodeAtTail(head, data):
    # if empty list
    if head == None:
        return SinglyLinkedListNode(data)

    # if list not empty
    firstHead = head
    while True:
        if head.next == None:
            head.next = SinglyLinkedListNode(data)
            return firstHead
        head = head.next
        

if __name__ == '__main__':

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n')
    print('\n')

