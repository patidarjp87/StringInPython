print('program to arrange words in a given string alphabatically\n Enter a string')
s=input()
s1=input("press enter to see sorted string")
l=s.split()
l.sort()
for x in l:
    s1+=x
    s1+=' '
s=s1
print(s)
input()
