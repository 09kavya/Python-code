#write a program to count the no. of consonants in the word "learning"

word="learning"
count=0
ch=0
while ch<len(word):
    if word[ch] not in "aeiou":
        count+=1
    ch += 1
print(count)