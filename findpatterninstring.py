print('program to find pattern in given string \n Enter a string')
s=input()
l=len(s)
for x in range(1,l):
 i=0
 j=x
 count=0
 while l!=j:
   if s[i:j:1]==s[i+x:j+x:1]:
     i+=x
     j+=x
     count+=1
   else :
     break
 else:
    print('pattern is',s[0:x:1])
    print('occurence of',s[0:x:1],"is",count+1)
    break
else:
    print('There is no fix pattern in',s)
input()
