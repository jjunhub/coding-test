class Node:
  def __init__(self, value, left, right):
    self.value = value
    self.left = left
    self.right = right

  def set_left(self, left) -> None:
    self.left = left
  
  def set_right(self, right) -> None:
    self.right = right

def preOrder(root : Node):
  if root == None:
    return
  print(root.value, end="")
  preOrder(root.left)
  preOrder(root.right)

def inOrder(root : Node):
  if root == None:
    return
  inOrder(root.left)
  print(root.value, end="")
  inOrder(root.right)

def postOrder(root : Node):
  if root == None:
    return
  postOrder(root.left)
  postOrder(root.right)
  print(root.value, end="")

N = int(input())
node_list = dict()

for _ in range(N):
  root, left, right = input().split()
  if left not in node_list :
    if left != "." :
      left_node = Node(left, None, None)
      node_list[left_node.value] = left_node
    else :
      left_node = None
  else :
    left_node = node_list[left]

  if right not in node_list:
    if right != "." :
      right_node = Node(right, None, None)
      node_list[right_node.value] = right_node
    else :
      right_node = None
  else :
    right_node = node_list[right]
  
  if root not in node_list:
    root_node = Node(root, left_node, right_node)
    node_list[root_node.value] = root_node
  else :
    root_node = node_list[root]
    root_node.set_left(left_node)
    root_node.set_right(right_node)

preOrder(node_list["A"])
print()
inOrder(node_list["A"])
print()
postOrder(node_list["A"])
print()