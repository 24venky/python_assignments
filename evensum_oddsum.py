number=[2,7,4,9,10,15]
even_sum=0
odd_sum=0
for num in number:
    if num%2==0:
        even_sum+=num
    else:
        odd_sum+=num
print(f"the even sum is {even_sum}")
print(f"the odd sum is {odd_sum}")
