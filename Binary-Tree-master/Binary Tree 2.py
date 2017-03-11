class TNode:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

class BST:
  def __init__(self, root):
    self._root = root

  def bfs(self):
    list = [self._root]
    i = 0
    while len(list) > 0:
        print ([e.data for e in list], i)
        i += 1 # Номер уровня
        list = [e.left for e in list if e.left] + \
               [e.right for e in list if e.right]
bst = BST(TNode(1, TNode(2, TNode(4), TNode(5)), TNode(3, TNode(6), TNode(7))))
bst.bfs()
