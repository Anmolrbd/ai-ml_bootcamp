class Student:
    
    def __init__(self,name,age,student_id,course):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.course = course
        
    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")
        print(f"Student Course: {self.course}")
        print()
    
    def change_course(self,new_course):
        if new_course == self.course:
            print("Same course.")
            return
        self.course = new_course
    
    def have_birthday(self):
        self.age += 1
    
student1 = Student("Alice",20,1,"BCT")
student2 = Student("Bob",24,2,"Civil")
student3 = Student("Charlie",25,3,"Electrical")

print("Before changes: ")
student1.display_info()
student2.display_info()
student3.display_info()

student1.change_course("Mechanical")
student2.have_birthday()

print("After changes: ")
student1.display_info()
student2.display_info()
student3.display_info()

