from operator import le


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_grade = 0
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name) 

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __calculation_avg_grade(self):
        count = 0      
        for grade in self.grades.values():
            self.avg_grade += sum(grade)
            for i in grade:
                count += 1
        self.avg_grade = self.avg_grade / count          
        return self.avg_grade
    
    def __lt__(self, other):
        if (not isinstance(self, Student)) or (not isinstance(other, Student)):
            return
        if other.avg_grade < self.avg_grade:
            print(f"Cредний балл выше у студента: {self.name}")
        else:
            print(f"Cредний балл выше у студента: {other.name}")
            
    def __str__(self) -> str:
        self.__calculation_avg_grade()
        return f"""
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.avg_grade}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {','.join(self.finished_courses)}
"""

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    
class Lecturer(Mentor):   
    def __init__(self, name, surname):
        super().__init__(name, surname)       
        self.grades = {}
        self.avg_grade = 0
    def __calculation_avg_grade(self):
        count = 0      
        for grade in self.grades.values():
            self.avg_grade += sum(grade)
            for i in grade:
                count += 1
        self.avg_grade = self.avg_grade / count          
        return self.avg_grade
    
    def __lt__(self, other):
        if (not isinstance(self, Lecturer)) or (not isinstance(other, Lecturer)):
            return 'Ошибка'
        if other.avg_grade < self.avg_grade:
            print(f"Cредний балл выше у лектора: {self.name}")
        else:
            print(f"Cредний балл выше у лектора: {other.name}")

    def __str__(self) -> str:
        self.__calculation_avg_grade()
        return f"""
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.avg_grade}
"""

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self) -> str:
        return f"""
Имя: {self.name}
Фамилия: {self.surname}
"""


# Test Task1
best_student = Student('Ruoy', 'Eman', 'mail')
best_student.courses_in_progress += ['Python', 'Git']
first_student = Student('Nik', 'Nikolaev', 'mail')
first_student.courses_in_progress += ['Python', 'Git']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 3)
cool_reviewer.rate_hw(first_student, 'Python', 10)
cool_reviewer.rate_hw(first_student, 'Python', 10)
cool_reviewer.rate_hw(first_student, 'Python', 6)

# print(best_student.grades)
# print(first_student.grades)

# Test Task2
cool_lecturer = Lecturer('Ivan', 'Ivanov')
cool_lecturer.courses_attached += ['Pyton']
first_lecturer = Lecturer('Vasya', 'Vasiliev')
first_lecturer.courses_attached += ['Pyton']

best_student.courses_in_progress += ['Pyton']

best_student.rate_hw(cool_lecturer, 'Pyton', 9)
best_student.rate_hw(cool_lecturer, 'Pyton', 9)
best_student.rate_hw(cool_lecturer, 'Pyton', 2)
best_student.rate_hw(first_lecturer, 'Pyton', 9)
best_student.rate_hw(first_lecturer, 'Pyton', 9)
best_student.rate_hw(first_lecturer, 'Pyton', 7)

# print(cool_lecturer.grades)

# Test Task3

best_student.add_courses('Введение в программирование')
first_student.add_courses('Введение в программирование')

print(cool_reviewer)

print(cool_lecturer)
print(first_lecturer)
is_lt = (first_lecturer < cool_lecturer)

print(best_student)
print(first_student)
best_student.__lt__(first_student)






# ..........


