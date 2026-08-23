#armstrong no. from 1 to 1000
for num in range(1, 1001):

    original = num
    digits = len(str(num))
    sum = 0

    for i in range(digits):
        digit = num % 10
        sum = sum + digit ** digits
        num = num // 10

    if sum == original:
        print(original)