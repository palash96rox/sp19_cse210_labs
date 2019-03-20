def fractional_knapsack(l,w):
  l = sorted(l, key=lambda x: x['value'], reverse=True)
  s,i = 0,0
  selected = []
  while (s+l[i]['weight'])<=w and i<len(l):
    s += l[i]['weight']
    selected.append(l[i])
    i+=1
  if i == len(l): return selected # exhausted items
  if s<w:
    d = w-s
    r = d/l[i]['weight']
    selected.append({
      'value': l[i]['value']*r,
      'weight': l[i]['weight']*r,
      'ratio': l[i]['ratio']
    })
  return selected

# Greedy solution: NP Hard
def knapsack(l,w):
  l = sorted(l, key=lambda x: x['ratio'], reverse=True)
  s,i = 0,0
  selected = []
  while (s+l[i]['weight'])<=w and i<len(l):
    s += l[i]['weight']
    selected.append(l[i])
    i+=1
  return selected
  
def get_list():
  n = int(input('Number of values: '))
  l = []
  print('Enter value and weight of each item below')
  for i in range(n):
    val = int(input('Value for item-'+str(i+1)+': '))
    wt = int(input('Weight for item-'+str(i+1)+': '))
    l.append({
      'value': val,
      'weight': wt,
      'ratio': val/wt
    })
  return l

if __name__ == '__main__':
  l = get_list()
  w = int(input('Knapsack capacity: '))
  k = knapsack(l,w)
  print('Value of knapsack: ' + str(sum(item['value'] for item in k)))
  print('Weight of knapsack: ' + str(sum(item['weight'] for item in k)))
  print('List: ' + ','.join(str((x['value'],x['weight'])) for x in k))
  fk = fractional_knapsack(l,w)
  print('Value of fractional-knapsack: ' + str(sum(item['value'] for item in fk)))
  print('Weight of fractional-knapsack: ' + str(sum(item['weight'] for item in fk)))
  print('List: ' + ','.join(str((x['value'],x['weight'])) for x in fk))