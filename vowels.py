print('program to count vowels in a given string\n Enter a string')
s=str(input())
count=0
for x in s:
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
        count+=1
print('no. of vowels are',count)
input('press enter to exit')