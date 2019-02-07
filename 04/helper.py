def divide_into_four(X):
  n = len(X)
  X11 = [[None]*n]*n
  X12 = [[None]*n]*n
  X21 = [[None]*n]*n
  X22 = [[None]*n]*n

  return (X11,X12,X21,X22)

def mat_sum(A,B,t='+'):
  n = len(A)
  
  C = [[None]*n]*n

  for i in range(n):
    for j in range(n):
      if t=='+': 
        C[i][j] = A[i][j]+B[i][j]
      elif t=='-': 
        C[i][j] = A[i][j]-B[i][j]

  return C

def mat_diff(A,B):
  return mat_sum(A,B,'-')