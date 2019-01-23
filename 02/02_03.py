# Recurrence Relation: T(n) = T(n-1) + 1
def reverse_array(arr,rev=[]):
  l = len(arr)-1
  if l+1==0: return rev
  return reverse_array(arr[:l],rev+[arr[l]])

arr = [int(x) for x in input("Enter elems: ").split()]
rev = reverse_array(arr)
print("Reverse of",arr,"is",rev)