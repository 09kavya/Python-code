#write a program to print the word "python" in reverse using a for loop

text="Python"
for i in range(len(text)-1,-1,-1):
    print(text[i], end=" ")