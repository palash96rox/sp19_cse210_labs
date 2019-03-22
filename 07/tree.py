class Min_Tree:
  def __init__(self, node=None):
    self.node = node
    self.children = []

  def print_tree(self, cost=0, depth=0):
    aesthetic = '-'*(depth*3) + '(' + str(cost) + ') Node: '
    print(aesthetic + str(self.node))
    for child in self.children:
      child[0].print_tree(child[1],depth+1)

# ERROR!!

def rem_from_list(l,x):
  index = l.index(x)
  return l[:index]+l[index+1:]

# TODO build from [(src,dst,wt),]
def build_tree(e,root=None,current=None):
  if not e: return root
  if not root: root = Min_Tree(e[0][0])
  if not current: current = root.node
  if len(e) == 1:
    leaf = Min_Tree(e[0][1])
    root.children.append((leaf,e[0][2]))
  else:  
    for edge in e:
      if edge[0] == current:
        root.children.append((build_tree(rem_from_list(e,edge)),edge[2]))
  return root

if __name__ == '__main__':

  e = [
    (0,2,8),
    (2,3,6),
    (3,1,4),
    (1,5,3),
    (0,6,2)
  ]
  root = build_tree(e)
  root.print_tree()