import random
import pprint

def create_graph(v,max_wt=0,undirected=False):
  g = [[0 for _ in range(v)] for _ in range(v)]
  ne = random.randint((v-1),(v*(v-1))) # Max edges
  w = [1] * ne
  if max_wt: 
    for i in range(ne): w[i] = random.randint(1,max_wt)
  while ne:
    src = random.randint(0,v-1)
    dst = random.randint(0,v-1)
    # print(src,dst)
    if g[src][dst]: continue
    ne-=1
    g[src][dst] = w[ne] # Reverse weights cuz dont want another variable
    if undirected: g[dst][src] = w[ne]
  return g

def min_tree(g):
  print('\nGraph:')
  pprint.pprint(g)

  print('-'*50)
  print('1. MST by Prim')
  print('2. MST by Kruskal')
  print('3. Multiple MST')
  c = int(input('?: '))

  import prim, kruskal

  if c==1: prim.prim(g)
  elif c==2: kruskal.kruskal(g)
  elif c==3:
    if len(g)<10:
      print('Graph too small')
      return
    print('Minimum Spanning Trees formed via Prim:')
    prim.prim(g)
    print('Minimum Spanning Trees formed via Kruskal:')
    kruskal.kruskal(g)
  else: print('Invalid')


if __name__ == '__main__':
  
  print('\n' + ('-'*50) + '\nlab07: Minimum Spanning Trees\n' + ('-'*50))

  while True:
    print()
    print('1: Enter Graph')
    print('2: Create Random Graph')
    print('3: Exit')
    c = int(input('?: '))

    if c==1 or c==2:
      v = int(input('Number of vertices: '))
      w = int(input('Weighted Graph [0/1]? '))
      d = int(input('Directed Graph [0/1]? '))

      if c==1:
        g = [[0 for _ in range(v)] for _ in range(v)]
        print('Enter edges below: [Nodes start from 0]')
        while c:
          src = int(input('Source node: '))
          dst = int(input('Destination node: '))
          wt = 1
          if w: wt = int(input('Cost of path: '))
          g[src][dst] = wt
          if not d:
            g[dst][src] = wt
          c = int(input('More edges [0/1]? '))

      elif c==2:
        if w: w = int(input('Max cost of path: '))
        g = create_graph(v,w,d==0)

      min_tree(g)

    elif c==3: break
    else: print('Invalid')

    print('-'*50)

  print('bye.')