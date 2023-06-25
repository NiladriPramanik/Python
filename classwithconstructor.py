class Student:

    def __init__ ( self, name, age, hieght, gender ):
          
        self.name=name
        self.age=age
        self.hieght=hieght
        self.gender=gender
    
    def employee_details(self):
        print("Student's name is ",self.name)
        print("Student's age is ",self.age)
        print(" Student's hieght in cm is",self.hieght)
        print("Student's gender is ",self.gender)

e1=Student('Niladri',23,178,'Male')

e1.employee_details()







