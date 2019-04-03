import pprint

def lcs(a,b):
  m,n = len(a),len(b)
  table = [[0]*(n+1) for _ in range(m+1)]
  l,sub = 0,''
  for i in range(m):
    for j in range(n):
      if a[i]==b[j]: 
        c = table[i][j] + 1
        table[i+1][j+1] = c
        if c>l:
          sub = a[i+1-c:i+1]
          l = c
        elif c==l: sub+=a[i+1-c:i+1]
  return sub

def lcs_seq(a,b):
  m,n = len(a),len(b)
  table = [[0]*(n+1) for _ in range(m+1)]
  for i in range(m):
    for j in range(n):
      if a[i]==b[j]: table[i+1][j+1] = table[i][j] + 1
      else: table[i+1][j+1] = max(table[i+1][j],table[i][j+1])
  sub = ''
  for i in range(m+1):
    if table[i][n] != table[i-1][n] and i!=0: 
      sub+=a[i-1]
  return sub

if __name__ == '__main__':
  a = input('str1: ')
  b = input('str2: ')
  print('Longest substring:',lcs(a,b))
  print('Longest subsequence:',lcs_seq(a,b))