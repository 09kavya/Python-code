#write aa program to reverse each word in the sentence " Hello World" using a while loop.

sentence="Hello World" 
words=sentence.split()
for word in words:
    num=len(word)-1

    while(num>=0):
        print(word[num],end=" ")
        num = num-1
    print(end=" ")