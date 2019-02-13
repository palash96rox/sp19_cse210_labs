from helper import *

def rec_mat_mul(A,B):
  if not len(A[0])==len(B): return None
  n = len(A)
  if n == 1:
    C = [[None]]
    C[0][0] = A[0][0]*B[0][0]
    return C
  
  A11,A12,A21,A22 = divide_into_four(A)
  B11,B12,B21,B22 = divide_into_four(B)

  C11 = mat_sum(rec_mat_mul(A11,B11),rec_mat_mul(A12,B21))
  C12 = mat_sum(rec_mat_mul(A11,B12),rec_mat_mul(A12,B22))
  C21 = mat_sum(rec_mat_mul(A21,B11),rec_mat_mul(A22,B21))
  C22 = mat_sum(rec_mat_mul(A21,B12),rec_mat_mul(A22,B22))

  return combine_into_one(C11,C12,C21,C22)