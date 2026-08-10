name=input("Enter the student name:")
student_id=int(input("Enter student id:"))
student_hallticket_num=int(input("Enter hall ticket number:"))
marks=int(input("Enter the marks:"))
if marks>=95:
    print("congratulations you get A+")
elif marks>=85:
    print("super you get A")
elif marks>=75:
     print("Great you get B")
elif marks>=65:
     print("nice you get C")
elif marks>=55:
      print("ok you get D")
elif marks>=45:
      print("study hard you get E")
else:
       print("sorry you are fail F")

