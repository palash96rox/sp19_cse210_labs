import sys

def mcm(arr,i,j):
  if i==j: return 0

  m = sys.maxsize

  for k in range(i,j):
    c = mcm(arr,i,k) + mcm(arr,k+1,j) + arr[i-1]*arr[k]*arr[j]
    if c<m: m=c

  return m

if __name__ == '__main__':
  arr = [1,2,2,3]
  n = len(arr)
  print('minimum multiplications for',arr,':',mcm(arr,1,n-1))

  c = int(input('Custom input? '))
  if c:
    n = int(input('Matrices: '))
    arr = []
    while n>0:
      r,c = int(input('Rows: ')),int(input("cols: "))
      if not arr: 
        arr.append(r)
        arr.append(c)
      else:
        if r!=arr[-1]:
          print('Rows do not match last column')
          continue
        arr.append(c)
      n-=1
  
  print('minimum multiplications needed:',mcm(arr,1,len(arr)-1))