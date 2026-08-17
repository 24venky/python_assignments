class Delivery:
    def charge(self,distance):
        self.distance = distance
        if 1<=self.distance<=1000:
            return self.distance*5

    def charge(self,distance,express):
        self.distance=distance
        self.express=express
        if 1<=self.distance<=1000 and 0<= self.express <=5000:
            return self.distance*5+self.express

distance=int(input("enter"))
express=int(input("enter"))
d=Delivery()
print(d.charge(distance,express))
