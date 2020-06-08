print("program to remove duplicate character in a given string\n Enter a string")
s=input()
s1=input('press enter to conitnue program')
c=0
for x in s:
    if c==0:
        c=1
        y=x
        s1=s1+y
    else:
        if x==y:
            continue
        else:
            s1=s1+x
            y=x
print(s1)
input()

