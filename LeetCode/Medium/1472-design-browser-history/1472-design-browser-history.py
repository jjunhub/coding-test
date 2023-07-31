class Node(object):
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = self.current = Node(val = homepage)
    def visit(self, url: str):
        self.current.next = Node(url, next = None, prev = self.current)
        self.current = self.current.next

    def back(self, steps: int):
        for _ in range(steps):
            if(self.current.prev == None) :
                break
            self.current = self.current.prev
        return self.current.val
    

    def forward(self, steps: int):
        for _ in range(steps):
            if(self.current.next == None):
                break
            self.current = self.current.next
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)