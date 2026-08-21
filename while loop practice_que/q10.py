#writa a program to count occurences of the character "s" in the string "success"

word=input("Enter the word= ")
char=input("Enter the character= ")

count=0
ch=0
while ch<len(word):
    if word[ch]==char:
        count +=1
    ch +=1
print(count)