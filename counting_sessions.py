day=5
session=2
count=0
for i in range(1,day+1):
    if i == 3:
        print("its a revision day")
        continue
    for j in range(1,session+1):
        if i==5:
            print(f"day {i} has only session{j}")
            count+=1
            break

        print(f"day{i}and session{j}")
        count+=1

print("target is archieved")
print("total classes attended is ",count)