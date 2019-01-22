def reverse_stack(stack,rev):
  pass

def reverse_string(string,rev=''):
  l = len(string)-1
  if l+1==0: return rev
  return reverse_string(string[:l],rev+string[l])

string = input("Enter String: ")
print(string,"reversed:",reverse_string(string))