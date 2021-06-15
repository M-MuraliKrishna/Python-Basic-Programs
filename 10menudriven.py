# 10. Demonstrate the i) Designing of a class ii) Creation of Object of that class iii) accessing the methods and instance variables in the class. 
# The student is at the liberty of choosing their own Description of the object for designing the class.

class person:
     def __init__(self,n,a):
          self.name=n
          self.age=a
     def ShowName(self):
           print("“Your Name:",self.name)
     def ShowAge(self):
           print("Your Age:",self.age)
class Student(person):
     def __init__(self,r,n,a):
           super().__init__(n,a)
           #person.__init__(self,n,a)
           self.rollno=r
     def ShowRollno(self):
            print("Your Roll No:",self.rollno)
name=input("Enter Your Name:")
age=int(input("Eneter your Age:"))
roll=(input("Enter Your Roll Number"))
obj=Student(roll,name,age)
obj.ShowRollno()
obj.ShowName()
obj.ShowAge()