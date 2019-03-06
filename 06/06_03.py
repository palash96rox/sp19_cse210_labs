def heapify(arr,n,i):
  maxi = i
  l,r = 2*i+1,2*i+2
  if l<n and arr[l]>arr[maxi]: maxi = l
  if r<n and arr[r]>arr[maxi]: maxi = r
  if maxi!=i:
    arr[maxi],arr[i] = arr[i],arr[maxi]
    heapify(arr,n,maxi)

def heapsort(arr):
  n = len(arr)
  for i in range(n,0,-1): heapify(arr,n,i)
  for i in range(n-1,0,-1):
    arr[i],arr[0] = arr[0],arr[i]
    heapify(arr,i,0)
  return arr

if __name__ == '__main__':
  arr = [22,5,6,85,24,26,25,53,20,19]
  print(heapsort(arr))