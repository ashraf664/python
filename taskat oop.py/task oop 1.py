class Person:
    def __init__(self, person_id, name, email):
        self.__id = person_id
        self.__name = name
        self.__email = email

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        self.__email = new_email

    def get_info(self):
        return f"Person: {self.__name} | Email: {self.__email}"

class Student(Person):
    def __init__(self, student_id, name, email, gpa=0.0):
        super().__init__(student_id, name, email)
        self.__gpa = gpa
        self.__enrolled_courses = []

    def enroll_course(self, course):
        self.__enrolled_courses.append(course)

    def get_courses(self):
        return self.__enrolled_courses

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, new_gpa):
        self.__gpa = new_gpa

    def get_info(self):
        courses_titles = [c.title for c in self.__enrolled_courses]
        return f"Student: {self.get_name()} | GPA: {self.__gpa} | Courses: {courses_titles}"


class Professor(Person):
    def __init__(self, prof_id, name, email, specialty):
        super().__init__(prof_id, name, email)
        self.__specialty = specialty
        self.__assigned_courses = []

    def assign_course(self, course):
        self.__assigned_courses.append(course)

    def get_courses(self):
        return self.__assigned_courses

    def get_specialty(self):
        return self.__specialty

    def set_specialty(self, new_specialty):
        self.__specialty = new_specialty

    def get_info(self):
        courses_titles = [c.title for c in self.__assigned_courses]
        return f"Professor: {self.get_name()} | Specialty: {self.__specialty} | Courses: {courses_titles}"
class Course:
    def __init__(self, code, title, credits):
        self.__code = code
        self.title = title
        self.credits = credits
        self.__professor = None
        self.__students = []

    def assign_professor(self, professor):
        self.__professor = professor
        professor.assign_course(self)

    def enroll_student(self, student):
        self.__students.append(student)
        student.enroll_course(self)

    def get_professor(self):
        return self.__professor

    def get_students(self):
        return self.__students

    def get_info(self):
        prof_name = self.__professor.get_name() if self.__professor else "None"
        students_names = [s.get_name() for s in self.__students]
        return f"Course: {self.title} | Code: {self.__code} | Prof: {prof_name} | Students: {students_names}"

s1 = Student(1, "ashraf", "ashraf@example.com", 3.5)
s2 = Student(2, "mohamed", "mohamed@gemail.com", 3.8)
p1 = Professor(1, "ENG. yosef", "joo@gemail.com", "Computer Science")
c1 = Course("m112", "Intro to Programming", 3)
c2 = Course("m110", "Data Structures", 4)
c1.assign_professor(p1)
c2.assign_professor(p1)
c1.enroll_student(s1)
c1.enroll_student(s2)
c2.enroll_student(s1)
print(s1.get_info())
print(s2.get_info())
print(p1.get_info())
print(c1.get_info())
print(c2.get_info())


