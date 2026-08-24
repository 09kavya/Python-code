# find the maximum consecutive 1s in a list

list1 = [1, 1, 0, 1, 1, 1, 0, 1]

count = 0
maximum = 0

for i in list1:
    if i == 1:
        count += 1

        if count > maximum:
            maximum = count
    else:
        count = 0

print("Maximum consecutive 1s =", maximum)