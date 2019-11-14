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


def printLinkedList(head):
    print(head.data)
    if head.next is not None:
        printLinkedList(head.next)


if __name__ == '__main__':
    n = int(input())
    inputData = []
    sll = SinglyLinkedList()

    for _ in range(n):
        sll.insert_node(int(input()))

    printLinkedList(sll.head)