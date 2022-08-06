import time

class school_info:
    def __init__(self,School_name,area,principal,total_strength):
        self.school_name=School_name
        self.area=area
        self.principal=principal
        self.total_strength=total_strength
    def info(self):
        print("School name is :",self.school_name)
        print("Area of school :  ",self.area)
        print("Name of the principal: ",self.principal)
        print("Total students of in a school : ",self.total_strength )
school_name=input("Enter a school name:")
area=input("Enter a location of school:")
principal=input("Enter a principal  name: ")
total_strength=int(input("Enter a no of students in a school:  "))
s1=school_info(school_name,area,principal,total_strength)
s1.info()