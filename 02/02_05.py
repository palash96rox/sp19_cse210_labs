def reverse_stack(stack,rev=[]):
  l = len(stack)-1
  if l+1==0: return rev
  return reverse_stack(stack[:l],rev+[stack[l]])

def reverse_string(string,rev=''):
  l = len(string)-1
  if l+1==0: return rev
  return reverse_string(string[:l],rev+string[l])

string = input("Enter String: ")
print(string,"reversed:",reverse_string(string))
stack = [int(x) for x in input("Enter elems: ").split()]
print(stack,"reversed:",reverse_stack(stack))