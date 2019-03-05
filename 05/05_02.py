def min_max(arr,low,high,min=None,max=None):
  if low == high: min,max = arr[low],arr[high]
  elif low == high-1:
    if arr[low] < arr[high]: min,max = arr[low],arr[high]
    elif arr[low] > arr[high]: min,max = arr[high],arr[low]
  else:
    mid = (low+high)//2
    min0 = max0 = arr[0]
    min1 = max1 = arr[mid]
    min0,max0 = min_max(arr,low,mid,min0,max0)
    min1,max1 = min_max(arr,mid,high,min1,max1)
    if min0<min1: min = min0
    else: min = min1
    if max0>max1: max = max0
    else: max = max1
  return (min,max)

if __name__ == '__main__':
  arr = [-1,-2,-3,-4,-5]
  print(min_max(arr,0,len(arr)-1))