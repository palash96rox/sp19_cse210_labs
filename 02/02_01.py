# Recurrence Relation: T(n) = T(n-1) + 2
def find_max(arr,max):
  if len(arr)==0: return max
  if arr[0]>max: max = arr[0]
  return find_max(arr[1:],max)

arr = [int(x) for x in input("Enter array elems: ").split()]
max = find_max(arr[1:],arr[0])
print("max in",arr,"is",max)