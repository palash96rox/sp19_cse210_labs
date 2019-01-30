def binary_reverse(n,binary=''):
  if n==0: return binary
  return binary_reverse(n//2,binary+str(n%2))

def find_binary(n):
  binary = binary_reverse(n)
  return '0b'+binary[::-1]

def exp(n,e):
  if e==0: return 1
  h = exp(n,e//2)
  if e%2==0: return h*h
  return h*h*n

n = int(input("Enter number: "))
e = int(input("Enter exponent: "))
print(n,"in binary:",find_binary(n))
print(n,"**",e,"=",exp(n,e))