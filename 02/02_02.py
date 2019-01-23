# Recurrence Relation: T(n) = T(n-1) + 1
def reverse(word,rev=''):
  l = len(word)-1
  if l+1==0: return rev
  return reverse(word[:l],rev+word[l])

word = input("Enter a word: ")
rev = reverse(word)
if(word==rev): print("Palindrome!")
else: print("Not")