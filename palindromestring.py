print('program to print whether a given string palindrome or not \n Enter a string')
s=input()
i=0
l=len(s)
while l//2!=i:
  if s[i]==s[l-1-i]:
      i+=1
      continue
  else:
      print(s,'is not a palindrome string')
      break
else:
    print(s,'is a palindrome')
input()
