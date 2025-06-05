# Node Class:
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    def constructLL(self, arr):
        head = None
        for data in arr:
            if(head==0):
                head = Node(data)
                temp = head
            else:
                temp.next = Node(data)
                temp = temp.next
        printLinkedList(head)  # Fixed: function name and call

def printLinkedList(head):  # Fixed: function name and syntax
    temp = head
    while temp:
        print(temp.data, end=" ")  # Fixed: correct attribute is data
        temp = temp.next

arr = list(map(int, input().split()))
Solution().constructLL(arr)  # Fixed: class instantiation and method call
