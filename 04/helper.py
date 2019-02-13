import datetime

def get_matrix_from_user(n):
  X = [[None for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      X[i][j] = int(input(str(i+1)+","+str(j+1)+": "))
  return X

def divide_into_four(X):
  n = len(X)
  X11 = X
  X12 = X
  X21 = X
  X22 = X
  # Rows
  while len(X11)>n//2:
    X11 = X11[:len(X11)//2]
    X12 = X12[:len(X12)//2]
    X21 = X21[len(X21)//2:]
    X22 = X22[len(X22)//2:]
  # Cols
  while len(X11[0])>n//2:
    for i in range(len(X11[0])//2):
      X11[i] = X11[i][:len(X11[i])//2]
      X12[i] = X12[i][len(X12[i])//2:]
      X21[i] = X21[i][:len(X21[i])//2]
      X22[i] = X22[i][len(X22[i])//2:]
  return (X11,X12,X21,X22)

def combine_into_one(X11,X12,X21,X22):
  n = len(X11)
  X = [[0 for _ in range(n*2)] for _ in range(n*2)]
  for i in range(n):
    for j in range(n):
      X[i][j] = X11[i][j]
      X[i][n+j] = X12[i][j]
      X[n+i][j] = X21[i][j]
      X[n+i][n+j] = X22[i][j]
  return X

def mat_sum(A,B,t='+'):
  n = len(A)
  C = [[None for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if t=='+': 
        C[i][j] = A[i][j]+B[i][j]
      elif t=='-': 
        C[i][j] = A[i][j]-B[i][j]
  return C

def mat_diff(A,B):
  return mat_sum(A,B,'-')

# For testing
def slow_mul(A,B):
  if len(A[0]) != len(B): return None
  C = [[0 for _ in range(len(A))] for _ in range(len(B[0]))]
  for i in range(len(A)):
    for j in range(len(B[0])):
      for k in range(len(B)):
        C[i][j] += A[i][k]*B[k][j]
  return C