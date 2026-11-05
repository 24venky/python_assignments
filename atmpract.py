balance=int(input())
withdraw=int(input())
if withdraw<=0:
    print("invalid amount")
elif withdraw>balance:
    print("insufficient balance")
else:
    balance=balance-withdraw
    print(f"remaining balance is {balance}")