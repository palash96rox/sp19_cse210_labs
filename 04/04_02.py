import helper

def get_sums(X):
  X11, X12, X21, X22 = helper.divide_into_four(X)

  Xr1 = helper.mat_sum(X11,X12)
  Xr2 = helper.mat_sum(X21,X22)
  Xc1 = helper.mat_diff(X11,X21)
  Xc2 = helper.mat_diff(X12,X22)
  Xd1 = helper.mat_sum(X11,X22)

  return (Xr1,Xr2,Xc1,Xc2,Xd1)

def get_products(A,B):
  A11, A12, A21, A22 = helper.divide_into_four(A)
  Ar1,Ar2,Ac1,Ac2,Ad1 = get_sums(A)

  B11, B12, B21, B22 = helper.divide_into_four(B)
  Br1,Br2,Bc1,Bc2,Bd1 = get_sums(B)

  P11 = mat_mul(A11,Bc2)
  P21 = mat_mul(A22,Bc1)
  Pr1 = mat_mul(Ar1,B22)
  Pr2 = mat_mul(Ar2,B11)
  Pc1 = mat_mul(Ac1,Br1)
  Pc2 = mat_mul(Ac2,Br2)
  Pd1 = mat_mul(Ad1,Bd1)

  return (P11,P21,Pr1,Pr2,Pc1,Pc2,Pd1)

def get_sub_mat(A,B):
  P11,P21,Pr1,Pr2,Pc1,Pc2,Pd1 = get_products(A,B)

  C11 = helper.mat_diff(helper.mat_diff(Pd1,Pr1),helper.mat_diff(P22,Pc2))
  C12 = helper.mat_sum(P11, Pr1)
  C21 = helper.mat_diff(Pr2,P22)
  C22 = helper.mat_diff(helper.mat_diff(Pd1,Pr2),helper.mat_diff(P11,Pc1))

  return (C11,C12,C21,C22)

# Algorithm source - https://www3.cs.stonybrook.edu/~rezaul/Fall-2012/CSE548/CSE548-lecture-3.pdf
def mat_mul(A,B):
  C11,C12,C21,C22 = get_sub_mat(A,B)

  n = len(A)

  C = [[None]*n]*n

  return C