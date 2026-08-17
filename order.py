class OrderCalculator:
    def __init__(self,price,quality):
        self.price=price
        self.quality=quality
    def subtotal(self):
        if 1<=self.price<=10000 and 1<=self.quality<=100:
          return  self.price*self.quality
    def finaltotal(self,delivery):
         self.delivery=delivery
         if 0<=self.delivery<=1000:
             return self.delivery

price=int(input("enter"))
quality=int(input("enter"))
delivery=int(input("enter"))

o=OrderCalculator(price,quality)
print("subtotal:",o.subtotal())
print("final total:",o.finaltotal(delivery)+o.subtotal())