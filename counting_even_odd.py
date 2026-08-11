
numbers=[5,-2,0,8,-7,0,4]
pos_count=0
neg_count=0
zero_count=0
for i in numbers:
    if i>0:
        pos_count+=1
    elif i<0:
        neg_count+=1
    else:
        zero_count+=1
print(f"postive count is {pos_count}")
print(f"negative count is {neg_count}")
print(f"zero count is {zero_count}")
