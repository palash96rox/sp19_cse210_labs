import datetime

p01 = __import__('05_01')
p02 = __import__('05_02')
p03 = __import__('05_03')

n = int(input("number of elems in array: "))
arr = []
for i in range(n): arr.append(int(input("Element number "+str(i)+": ")))
print("array entered:",arr)
c = int(input("\n1.Quicksort, 2. Mergesort, 3. Find max and min? "))
CALL = datetime.datetime.now()
if c==1:
  arr = p01.quicksort(arr,0,len(arr)-1)
  print("Sorted",arr)
  print("Time:",datetime.datetime.now()-CALL)
elif c==2:
  arr = p03.mergesort(arr,0,len(arr)-1)
  print("Sorted",arr)
  print("Time:",datetime.datetime.now()-CALL)
elif c==3:
  min,max = p02.min_max(arr,0,len(arr)-1)
  print("Min,Max:",min,max)
  print("Time:",datetime.datetime.now()-CALL)
else:
  print("invalid")