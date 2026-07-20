class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age,student_id,course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course
    
    def display_student_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        print(f"Student Course: {self.course}")
        print()

    def study(self):
        print(f"{self.name} is studying {self.course}")   
        print()

class Teacher(Person):

    def __init__(self, name, age,teacher_id,subject):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.subject = subject
    
    def display_teacher_info(self):
        super().display_info()
        print(f"Teacher ID: {self.teacher_id}")
        print(f"Subject: {self.subject}")
        print()

    def teach(self):
        print(f"{self.name} is teaching {self.subject}")
        print()

student1 = Student("Harry",19,1,"Civil")
student1.display_student_info()
student1.study()

teacher1 = Teacher("Max",30,45,"Science")
teacher1.display_teacher_info()
teacher1.teach()