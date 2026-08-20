#write a program to count the no. of vowels in word "education"


word="education"
count=0
for ch in word:
    if ch in  "aeiou":
        count+=1
print(count)