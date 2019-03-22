'''Source: Geeks for Geeks
https://www.geeksforgeeks.org/kruskals-algorithm-simple-implementation-for-adjacency-matrix/
'''

def find(parent,x):
  if parent[x] == x: return x
  return find(parent,parent[x])

def union(parent,rank,x,y):
  xr,yr = find(parent,x),find(parent,y)
  if rank[xr]<rank[yr]: parent[xr] = yr
  elif rank[xr]>rank[yr]: parent[yr] = xr
  else:
    parent[yr] = xr
    rank[xr] += 1
  return parent,rank

def kruskal(mat):
  v = len(mat)
  g = []
  for i in range(v):
    for j in range(v):
      if mat[i][j]: g.append([i,j,mat[i][j]])
  g = sorted(g,key=lambda x:x[2])

  res = []

  parent = []
  for node in range(v): parent.append(node)
  rank = [0]*v

  i,e=0,0
  while e<v-1:
    src,dst,wt = g[i]
    s,d = find(parent,src),find(parent,dst)
    if s!=d:
      res.append(g[i])
      parent,rank = union(parent,rank,s,d)
      e+=1    
    i+=1

  # Print MST
  s = 0
  print('Edge\t\tWeight')
  for src,dst,wt in res: 
    print('%d - %d\t\t%d' % (src,dst,wt))
    s += wt
  print('Minimum Cost:',s)

if __name__ == '__main__':
  g = [[0, 29, 8, 0], [29, 0, 0, 4], [8, 0, 0, 6], [0, 4, 6, 0]]
  kruskal(g)
  g = [[0, 2, 0, 6, 0], 
        [2, 0, 3, 8, 5], 
        [0, 3, 0, 0, 7], 
        [6, 8, 0, 0, 9], 
        [0, 5, 7, 9, 0]]
  kruskal(g)

''' Incorrect for some reason. Gotta submit asap
from tree import Min_Tree

def kruskal(g):
  pass
'''