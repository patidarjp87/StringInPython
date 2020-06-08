print("program to count char in a given string \n Enter a string")
s=input()
count=0
for x in s:
    if (ord(x)>=65 and ord(x)<=90) or (ord(x)>=97 and ord(x)<=122):
        count+=1
print('no. of char in a given string are',count)
input()