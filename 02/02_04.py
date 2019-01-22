def fib(n,a=0,b=1):
  if n==0: return a
  if n==1: return b
  c = a+b
  d = b+c
  return fib(n-2,c,d)

def fact(n,p=1):
  if n==1: return p
  return fact(n-1,p*n)

n = int(input("Enter n: "))
print(n,"factorial:",fact(n))
print(n,"th fibonacci:",fib(n))