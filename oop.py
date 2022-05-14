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

    def calculation_avg_grade(self):
        strl = []       
        for _, grades_list in self.grades.items():
            strl.extend(grades_list)
        if len(strl) != 0:
            avg_grade = sum(strl) / len (strl)
            return avg_grade
        return 0
          
 
    def __lt__(self, other):
        if (not isinstance(self, Student)) or (not isinstance(other, Student)):
            return
        if other.avg_grade < self.avg_grade:
            print(f"Cредний балл выше у студента: {self.name}")
        else:
            print(f"Cредний балл выше у студента: {other.name}")
            
    def __str__(self) -> str:
        self.calculation_avg_grade()
        res = f"""
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.avg_grade}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {','.join(self.finished_courses)}
"""
        return res

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
    
    def calculation_avg_grade(self):
        strl = []       
        for _, grades_list in self.grades.items():
            strl.extend(grades_list)
        if len(strl) != 0:
            avg_grade = sum(strl) / len (strl)
            return avg_grade
        return 0

    def __lt__(self, other):
        if (not isinstance(self, Lecturer)) or (not isinstance(other, Lecturer)):
            return 'Ошибка'
        if other.avg_grade < self.avg_grade:
            print(f"Cредний балл выше у лектора: {self.name}")
        else:
            print(f"Cредний балл выше у лектора: {other.name}")

    def __str__(self) -> str:
        self.calculation_avg_grade()
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


# STUDENTS:

first_student = Student('Ivan', 'Ivanov', 'mail')
first_student.add_courses('Введение в программирование')
first_student.courses_in_progress += ['Python', 'Git']

print(first_student)

second_student = Student('Olesya', 'Ivanova', 'femail')
second_student.add_courses('Введение в программирование')
second_student.courses_in_progress += ['Python', 'Git']

print(second_student)

# LECTURERS:

first_lecturer = Lecturer('Petr', 'Petrov')
first_lecturer.courses_attached += ['Python', 'Git']

print(first_lecturer)

second_lecturer = Lecturer('Inna', 'Petrova')
second_lecturer.courses_attached += ['Python', 'Git']

print(second_lecturer)

# REVIEWERS:

first_reviewer = Reviewer('Petr', 'Petrov')
first_reviewer.courses_attached += ['Python', 'Git']

print(first_reviewer)

second_reviewer = Reviewer('Inna', 'Petrova')
second_reviewer.courses_attached += ['Python', 'Git']

print(second_reviewer)

# STUDENTS rate_hw:

first_student.rate_hw(first_lecturer, 'Python', '10')
first_student.rate_hw(first_lecturer, 'Python', '8')
first_student.rate_hw(first_lecturer, 'Git', '10')
first_student.rate_hw(first_lecturer, 'Git', '6')
first_student.rate_hw(second_lecturer, 'Python', '9')
first_student.rate_hw(second_lecturer, 'Python', '7')
first_student.rate_hw(second_lecturer, 'Git', '9')
first_student.rate_hw(second_lecturer, 'Git', '5')

second_student.rate_hw(first_lecturer, 'Python', '10')
second_student.rate_hw(first_lecturer, 'Python', '8')
second_student.rate_hw(first_lecturer, 'Git', '10')
second_student.rate_hw(first_lecturer, 'Git', '6')
second_student.rate_hw(second_lecturer, 'Python', '9')
second_student.rate_hw(second_lecturer, 'Python', '7')
second_student.rate_hw(second_lecturer, 'Git', '9')
second_student.rate_hw(second_lecturer, 'Git', '5')

# REVIEWERS rate_hw:

first_reviewer.rate_hw(first_student, 'Python', '10')
first_reviewer.rate_hw(first_student, 'Python', '8')
first_reviewer.rate_hw(first_student, 'Git', '10')
first_reviewer.rate_hw(first_student, 'Git', '6')
first_reviewer.rate_hw(second_student, 'Python', '9')
first_reviewer.rate_hw(second_student, 'Python', '7')
first_reviewer.rate_hw(second_student, 'Git', '9')
first_reviewer.rate_hw(second_student, 'Git', '5')

second_reviewer.rate_hw(first_student, 'Python', '10')
second_reviewer.rate_hw(first_student, 'Python', '8')
second_reviewer.rate_hw(first_student, 'Git', '10')
second_reviewer.rate_hw(first_student, 'Git', '6')
second_reviewer.rate_hw(second_student, 'Python', '9')
second_reviewer.rate_hw(second_student, 'Python', '7')
second_reviewer.rate_hw(second_student, 'Git', '9')
second_reviewer.rate_hw(second_student, 'Git', '5')

is_lt = (first_student < second_student)
first_lecturer.__lt__(second_lecturer)