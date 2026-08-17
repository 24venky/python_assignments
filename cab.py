class CabBooking:
    def __init__(self,passengerName,cabType,distane):
        self.passengerName=passengerName
        self.cabType=cabType
        self.distance=distane
    def displayBooking(self,choice):
        if choice==1:
            self.fare=75
            print("passenger Name:",self.passengerName)
            print("cab Type :",self.cabType)
            print("distance :",self.distance,"km")
            print("fare RS:",self.fare)
        elif choice==2:
            self. fare=self.distance*15
            print("passenger Name:", self.passengerName)
            print("cab Type :", self.cabType)
            print("distance :", self.distance, "km")
            print("fare RS:", self.fare)
        else:
            print("invalid choice")

choice=int(input("enter your choice:"))
name=input("enter name:")
if choice==1:
    cabType = "mini"
    distance = 5
    fare = 75

if choice==2:
    cabType=input(" enter cab Type :")
    distance=int(input("enter distance:"))
cb=CabBooking(name,cabType,distance)
cb.displayBooking(choice)

