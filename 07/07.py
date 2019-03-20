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
  pass


if __name__ == '__main__':
  print()
  print('\nWelcome to graphs!!')
  while True:
    print()
    print('1: Enter Graph')
    print('2: Create Random Graph')
    print('3: Exit')
    c = int(input('?: '))

    if c==1:
      v = int(input('Number of vertices: '))
      g = [[0 for _ in range(v)] for _ in range(v)]
      # TODO: Input graph
      min_tree(g)

    elif c==2:
      v = int(input('Number of vertices: '))
      w = int(input('Max Weight for edges [0 for unweighted]? '))
      d = int(input('Directed [1/0]? '))
      g = create_graph(v,w,d==1)
      min_tree(g)

    elif c==3:
      print('bye.')
      exit(0)