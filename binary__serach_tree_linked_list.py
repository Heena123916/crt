class Node:
    def __init__(self, data):
        self.left = None
        self.val = data
        self.right = None

def createBST(arr):
    root = None
    for data in arr:
        if root == None:
            root = Node(data)
        else:
            temp = root
            while True:
                # smaller element
                if data < temp.val:
                    if temp.left == None:
                        temp.left = Node(data)
                        break
                    else:
                        temp = temp.left
                # largest element
                elif data > temp.val:
                    if temp.right == None:
                        temp.right = Node(data)
                        break
                    else:
                        temp = temp.right

    print(root.left.right.val)  # -> 3

arr = list(map(int, input().split()))
createBST(arr)
