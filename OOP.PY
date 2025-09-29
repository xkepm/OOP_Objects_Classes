class Student:
    school = "AI University"
    student_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.student_count += 1


s1 = Student("Meshal", 16)
s2 = Student("Shaden", 13)
print(s1.name, s1.age, s1.school)
print(s2.name, s2.age, s2.school)

s1.age = 23
print(s1.age, s2.age)

Student.school = "Tech Academy"
print(s1.school, s2.school)

print("Total students:", Student.student_count)
