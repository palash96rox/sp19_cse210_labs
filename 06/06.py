import datetime

p01 = __import__('06_01')
p02 = __import__('06_02')
p03 = __import__('06_03')

n = int(input("number of elems in array: "))
arr = []
for i in range(n): arr.append(int(input("Element number "+str(i)+": ")))
print("array entered:",arr)
c = int(input("\n1.Countsort, 2. Shellsort, 3. Heapsort? "))
CALL = datetime.datetime.now()
if c==1:
  arr = p01.countsort(arr,max(arr))
  print("Sorted",arr)
  print("Time:",datetime.datetime.now()-CALL)
elif c==2:
  arr = p02.shellsort(arr)
  print("Sorted",arr)
  print("Time:",datetime.datetime.now()-CALL)
elif c==3:
  arr = p03.heapsort(arr)
  print("Sorted:",arr)
  print("Time:",datetime.datetime.now()-CALL)
else:
  print("invalid")