def palindrome(name):
    if len(name)<=1:
        return "It is palindrome"
    if name[0] != name[-1]:
        return "It is not palindrome"

    return palindrome(name[1:-1])

a=palindrome("Madam")

print(a)
