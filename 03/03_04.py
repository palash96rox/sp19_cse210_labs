# Extended master's theorem: T(n) = aT(n/b)+O(n**k(logn)**i)
# chr(920) = Θ; chr(8712) = ∈
import math

def get_complexity(k,i):
  string = ''
  return string

def master(a,b,k,i):
  error = 'Error in input: '
  flag = False
  if a<1: 
    flag = True
    error+='a must be non negative; '
  if b<=1: 
    flag = True
    error+='b must atleast be 1; '
  if k<0: 
    flag = True
    error+='k must be non negative; '
  if i<0: 
    flag = True
    error+='i must be non negative; '
  if flag: return error
  # Recurrence relation
  reccurence = 'T(n):= ' 
  if a==0: reccurence += '0'
  else: reccurence += ('' if a==1 else str(a)) + 'T(n' + ('' if b==1 else '/'+str(b)) + ')'
  reccurence += ' + ' + chr(920) + '[' + get_complexity(k,i) + ']'
  # Complexity
  solution = 'T ' + chr(8712) + ' ' + chr(920) + '('
  p = math.log(a)/math.log(b)
  if p==k: solution += get_complexity(k,i+1)
  elif p<k: solution += get_complexity(k,i)
  else:
    if round(p) == p: solution += get_complexity(round(p),0)
    else: solution += 'nigga wut'
  solution += ')'
  return reccurence,solution

print(master(1,2,3,4))