'''Source: Geeks for Geeks
https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
'''
import sys

def print_tree(g,parent):
  s=0
  print('Edge\t\tWeight')
  for i in range(1,len(g)):
    print(parent[i],'-',i,'\t\t',g[i][parent[i]])
    s+=g[i][parent[i]]
  print('Minimum Cost:',s)

def minKey(key,mstSet,v): 
  min = sys.maxsize 
  for x in range(v): 
    if key[x] < min and mstSet[x] == False: 
      min = key[x] 
      min_index = x 
  return min_index

def prim(g,start=0):
  v = len(g)
  key = [sys.maxsize] * v
  parent = [None] * v
  mstSet = [False] * v

  key[0] = start
  parent[0] = -1 

  for cout in range(v):
    u = minKey(key,mstSet,v) 
    mstSet[u] = True
    for x in range(v):
      if g[u][x] > 0 and mstSet[x] == False and key[x] > g[u][x]: 
        key[x] = g[u][x] 
        parent[x] = u
  print_tree(g,parent)

if __name__ == '__main__':
  g = [[0, 29, 8, 0], [29, 0, 0, 4], [8, 0, 0, 6], [0, 4, 6, 0]]
  prim(g)
  g = [[0, 2, 0, 6, 0], 
        [2, 0, 3, 8, 5], 
        [0, 3, 0, 0, 7], 
        [6, 8, 0, 0, 9], 
        [0, 5, 7, 9, 0]]
  prim(g)


''' Self try

DOESN'T work cuz of Tree

from tree import Min_Tree

def get_src(g,v):
  costs = []
  for s in v: costs.append((s,g[s]))
  src = v[0]
  min = max(max(c[1]) for c in costs)
  for c in costs:
    m = min
    for x in c[1]:
      if x and x<m: m = x
    if m<min: src,min = c[0],m
  return src,min

def prim(g,start=0,v=[],root=None,current=None):
  if len(v) == len(g)-1: return root
  if not root: root = Min_Tree(start)
  if not current: current = root
  v.append(start)
  src,min = get_src(g,v)
  dst = g[src].index(min)
  child = Min_Tree(dst)
  current.children.append((child,min))
  root.print_tree()
  return prim(g,dst,v,root,child)


# testing
if __name__=='__main__':
  g = [[0, 29, 8, 0], [29, 0, 0, 4], [8, 0, 0, 6], [0, 4, 6, 0]]
  root = prim(g)
  root.print_tree()
  root = prim(g,start=1)
  root.print_tree()

'''