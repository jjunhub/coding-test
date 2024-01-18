import sys
input = sys.stdin.readline

class node:
    def __init__(self, val = 0, next = None, prev = None):
        self.val = 0
        self.next = next
        self.prev = prev

def showNodes(head):
    cur = head
    if cur.val == "#":
        cur = cur.next
    while cur:
        print(cur.val, end="")
        cur = cur.next
    print()

testcase = int(input())
for _ in range(testcase):
    inputValue = input().rstrip()
    head = node()
    head.val = "#"
    current = head

    for char in inputValue:
        # print(f'char = {char}, current = {current}')
        if char == "<":
            current = current.prev if current.prev != None else current
        elif char == ">":
            current = current.next if current.next != None else current
        elif char == "-":
            if current.prev != None:
                current.prev.next = current.next
                if current.next != None :
                    current.next.prev = current.prev
                current = current.prev
            
        else :
            newNode = node()
            newNode.val = char
            if current.next == None:
                current.next, newNode.prev = newNode, current
                current = current.next
            else :
                newNode.next, current.next.prev = current.next, newNode
                current.next, newNode.prev = newNode, current
                current = current.next
            
    showNodes(head)