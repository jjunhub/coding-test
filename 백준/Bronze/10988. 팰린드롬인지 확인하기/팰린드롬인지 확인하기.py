word = input()

def isPalindrome():
  reversedWord = word[::-1]
  for idx in range(len(word)):
    if word[idx] != reversedWord[idx]:
      return False
  else :
    return True

if isPalindrome() :
  print("1")
else :
  print("0")

