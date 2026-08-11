num=int(input("Enter upto a number:"))
stop=int(input("Enter a number where u want to stop"))
for i in range(1,num+1):
     if i-1==stop:
        break
     print(i)
