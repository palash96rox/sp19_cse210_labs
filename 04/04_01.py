def rec_mat_mul(A,B):

  if not len(A[0])==len(B): return None

  N = len(A) # A.rows [Ideally, nxn . nxn]
  if N==1:
    return A[0][0]*B[0][0]
  
  n = N//2
  A11 = [[None]*n]*n
  A12 = [[None]*n]*n
  A21 = [[None]*n]*n
  A22 = [[None]*n]*n
  B11 = [[None]*n]*n
  B12 = [[None]*n]*n
  B21 = [[None]*n]*n
  B22 = [[None]*n]*n

  C11 = rec_mat_mul(A11,B11) + rec_mat_mul(A12,B21)
  C12 = rec_mat_mul(A11,B12) + rec_mat_mul(A12,B22)
  C21 = rec_mat_mul(A21,B11) + rec_mat_mul(A22,B21)
  C22 = rec_mat_mul(A21,B12) + rec_mat_mul(A22,B22)
