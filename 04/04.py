# python 3.6
# only for n * n where n = 2^k and k = 0,1,2,3,..
import datetime, pprint

p01 = __import__('04_01')
p02 = __import__('04_02')
helper = __import__('helper')

def is_power_of_two(n):
  return n!=0 and (n & (n-1))==0

def check_same(n=4):
  print("n =",n)
  if not is_power_of_two(n): assert False, 'n must be 2^k'

  START = datetime.datetime.now()
  A = [[0 for _ in range(n)] for _ in range(n)]
  B = [[0 for _ in range(n)] for _ in range(n)]
  END = datetime.datetime.now()
  print("Matrix creation:",END-START)

  START = datetime.datetime.now()
  C = helper.slow_mul(A,B)
  END = datetime.datetime.now()
  print("Iterative:",END-START)

  START = datetime.datetime.now()
  c1 = p01.rec_mat_mul(A,B)
  END = datetime.datetime.now()
  print("Recursive:",END-START)

  START = datetime.datetime.now()
  c2 = p02.mat_mul(A,B)
  END = datetime.datetime.now()
  print("Strassen:",END-START)
  
  assert C == c1, "Recursive is wrong"
  assert C == c2, "Strassen is wrong"

msg = "1. Random matrices for some n\n"
msg += "2. Enter your own matrix\n"
msg += "please choose: "
choice = int(input(msg))
if choice == 1:
  n = int(input("Enter the max power of two to be tested [len(matrix) = 2^n]: "))
  for i in range(n): check_same(2**i)
elif choice == 2:
  n = int(input("Enter n: "))
  A = helper.get_matrix_from_user(n)
  B = helper.get_matrix_from_user(n)

  START = datetime.datetime.now()
  C = helper.slow_mul(A,B)
  END = datetime.datetime.now()
  print("Iterative:",END-START)

  START = datetime.datetime.now()
  p01.rec_mat_mul(A,B)
  END = datetime.datetime.now()
  print("Recursive:",END-START)

  START = datetime.datetime.now()
  p02.mat_mul(A,B)
  END = datetime.datetime.now()
  print("Strassen:",END-START)

  print("Sum:")
  pprint.pprint(C)