def merge(arr, low, mid, high):
  l = mid-low+1
  r = high-mid
  L,R = [],[]
  for i in range(l): L.append(arr[low+i])
  for i in range(r): R.append(arr[mid+1+i])

  i,j,k = 0,0,low

  while i<l and j<r:
    if L[i]<R[j]:
      arr[k] = L[i]
      i+=1
    else:
      arr[k] = R[j]
      j+=1
    k+=1

  while i<l:
    arr[k] = L[i]
    i,k = i+1,k+1
  while j<r:
    arr[k] = R[j]
    j,k = j+1,k+1
  

def mergesort(arr,low,high):
  if low<high:
    mid = (low+high)//2
    mergesort(arr,low,mid)
    mergesort(arr,mid+1,high)
    merge(arr,low,mid,high)
  return arr

arr = [5,4,3,2,1]
print(mergesort(arr,0,len(arr)-1))