#Write a program that uses a while loop to find no. of vowels in given input string of lowercase latin letters.

s = input()
s.lower()
i=0
count =0
while i<len(s):
    if s[i]== 'a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
        count+=1
    i+=1
print(count)
