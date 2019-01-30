# Binary search for ascending order
# Requires: array, integer to find, start index, end index
def binary_search(arr,x,l,r):
  if l>r: return -1
  m = (l+r)//2
  if arr[m]>x: return binary_search(arr,x,0,m-1)
  elif arr[m]<x: return binary_search(arr,x,m+1,r)
  return m

n = int(input("Enter num of elements: "))
arr = []
print("Enter elements")
for _ in range(n): arr.append(int(input()))
print("Entered array:",arr)
arr = sorted(arr)
print("Sorted array:",arr)
x = int(input("Enter number to search: "))
print(x,'at position',binary_search(arr,x,0,n))