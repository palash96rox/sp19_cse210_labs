def find_sum(n,sum=0):
  if n==0: return sum
  return find_sum(n//10,sum+(n%10))

n = int(input("Enter number: "))
print("sum of digits:",find_sum(n))