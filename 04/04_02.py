from helper import *

# Strassen Matrix Multiplication
def mat_mul(A,B):
  if len(A) != len(B): return None
  n = len(A)
  if n == 1:
    C = [[0]]
    C[0][0] = A[0][0]*B[0][0]
    return C
  C = [[0 for _ in range(n)] for _ in range(n)]

  A11,A12,A21,A22 = divide_into_four(A)
  B11,B12,B21,B22 = divide_into_four(B)

  P1 = mat_mul(mat_sum(A11,A22),mat_sum(B11,B22))
  P2 = mat_mul(mat_sum(A21,A22),B11)
  P3 = mat_mul(A11,mat_diff(B12,B22))
  P4 = mat_mul(A22,mat_diff(B21,B11))
  P5 = mat_mul(mat_sum(A11,A12),B22)
  P6 = mat_mul(mat_diff(A21,A11),mat_sum(B11,B12))
  P7 = mat_mul(mat_diff(A12,A22),mat_sum(B21,B22))

  C11 = mat_sum(mat_diff(mat_sum(P1,P4),P5),P7)
  C12 = mat_sum(P3,P5)
  C21 = mat_sum(P2,P4)
  C22 = mat_sum(mat_diff(mat_sum(P1,P3),P2),P6)

  return combine_into_one(C11,C12,C21,C22)

# src: https://stackoverflow.com/questions/12867099/strassen-matrix-multiplication-close-but-still-with-bugs