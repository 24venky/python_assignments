numbers = [10, 25, 8, 40, 15]

largest = 0
second = 0

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second:
        second = num

print("Largest =", largest)
print("Second Largest =", second)