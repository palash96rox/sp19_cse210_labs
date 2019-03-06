def countsort(arr,maxval):
  count = [0]*(maxval+1)
  for x in arr: count[x] += 1
  index = 0
  for x in range(maxval+1):
    for _ in range(count[x]):
      arr[index] = x
      index += 1
  return arr

if __name__ == '__main__':
  arr = [56,85,74,22,23]
  print(countsort(arr,max(arr)))