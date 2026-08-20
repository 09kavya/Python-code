#write a progrm to count occurences of each character in the word "programming"


word="programming"
char_count={}

for char in word:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1

for char,count in char_count.items():
    print(char + ":" , count)