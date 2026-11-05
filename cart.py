def order():
    menu={"sandwitch":120,"juice":60,"pizza":250,"burgur":100}
    print("**********welcome to kafe**************")
    for r,v in menu.items():
       print(f"item: {r}  price: {v}")
    print("=======place your oder=======")
    list=[]
    discount=0
    deliveryFee=40
    subtotal=0
    place=True
    while place:
        print("place order (y/n):",end=" ")
        choice = input().lower()
        if choice != "n":
            item=input(" enter your item:")
            quantity=int(input(" "))
            list.append(item)
            print(f"item ordered: {item} and quantity: {quantity}")
            subtotal+=menu[item]*quantity
            print(subtotal)
        else:
            place=False
    print("########### your Bill ###############")
    if subtotal >= 500:
        discount = (subtotal * 10) / 100
        subtotal -= discount
        total = (subtotal + deliveryFee) - discount
        if subtotal >= 700:
            deliveryFee = 0
            total = (subtotal + deliveryFee) - discount
        else:
                total = (subtotal + deliveryFee) - discount
                print(f"food subtotal : {subtotal}")
                print(f"discount : {discount}")
                print(f" your total : {total}")

if __name__=="__main__":
    order()


