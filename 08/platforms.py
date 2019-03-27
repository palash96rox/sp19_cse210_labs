def get_arrivals():
  print()
  arr = []
  inp = int(input('Arrival time (-1 to end): '))
  while inp != -1:
    arr.append(inp)
    inp = int(input('Arrival time (-1 to end): '))
  return sorted(arr)

def get_departures():
  print()
  dep = []
  inp = int(input('Departure time (-1 to end): '))
  while inp != -1:
    dep.append(inp)
    inp = int(input('Departure time (-1 to end): '))
  return sorted(dep)

''' Takes sorted arrays '''
def min_platforms(arr,dep):
  print()
  used,total = 0,0
  a,d = 0,0
  while a<len(arr) and d<len(dep):
    if arr[a]<dep[d]:
      used+=1
      a+=1
    elif arr[a]>dep[d]:
      used-=1
      d+=1
    else:
      if total-used == 1: used += 1
      a+=1
      d+=1
    if used>total: total = used
  if a<len(arr): total += len(arr)-a
  return total