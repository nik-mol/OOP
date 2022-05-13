from operator import le


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_course.append(course_name) 

    def rate_evaluations(self, lecturer, course, evaluations):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.evaluations:
                lecturer.evaluations[course] += [evaluations]
            else:
                lecturer.evaluations[course] = [evaluations]
        else:
            return 'Ошибка'
 
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    
class Lecturer(Mentor):          
        evaluations = {}

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Test Task1
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)

# Test Task2
cool_lecturer = Lecturer('Ivan', 'Ivanov')
cool_lecturer.courses_attached += ['Pyton']

cool_student = Student('Petr', 'Petrov', 'mail')
cool_student.courses_in_progress += ['Pyton']

cool_student.rate_evaluations(cool_lecturer, 'Pyton', 9)
cool_student.rate_evaluations(cool_lecturer, 'Pyton', 9)
cool_student.rate_evaluations(cool_lecturer, 'Pyton', 9)

print(cool_lecturer.evaluations)

# ..........


