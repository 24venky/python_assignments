class Student:
    def __init__(self,name):
        self.name=name
    def showscore(self,score):
        self.score=score
        return self.score
    def showscore(self,score1,score2):
        self.score1=score1
        self.score2=score2
name=input("enter")
s=Student(name)
first_score=int(input("enter"))
second_score=int(input("enter"))
print("student name :",s.name)
s.showscore(first_score,second_score)
print("first score:",s.score1)
print("second score total:",s.score2+s.score1)



