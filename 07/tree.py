class Min_Tree:
  def __init__(self, node=None):
    self.node = node
    self.children = []

  def print_tree(self, cost=0, depth=0):
    aesthetic = '-'*(depth*3) + '(' + cost + ') Node: '
    print(aesthetic + self.node)
    for child in self.children: 
      child[0].print_tree(child[1],depth+1)

def is_equal(tree1,tree2):
  pass
