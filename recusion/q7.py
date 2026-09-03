"""
Reverse a string using recursion

Input: "hello"
Output: "olleh"

"""
def reverse(word):
    if word == '':
        return ""

    return reverse(word[1:]) + word[0]

print(reverse("hello"))
    