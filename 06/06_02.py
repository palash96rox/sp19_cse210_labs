def gap_insertion(arr,start,gap):
  for i in range(start,len(arr),gap):
    current = arr[i]
    pos = i
    while pos>=gap and arr[pos-gap]>current:
      arr[pos] = arr[pos-gap]
      pos = pos-gap
    arr[pos] = current
  return arr

def shellsort(arr):
  gap = len(arr)//2
  while gap > 0:
    for start in range(gap):
      arr = gap_insertion(arr,start,gap)
    gap //= 2
  return arr

if __name__ == '__main__':
  arr = [55,85,74,98,22,45,56]
  print(shellsort(arr))