from abc import ABC

class Person(ABC):
    def __init__(self):
        super().__init__()

    def get_role(self):
        pass



class Student(Person):
    def __init__(self):
        super().__init__()

    def get_roles(self):
        return "STUDENT"

class Instructor(Person):
    def __init__(self):
        super().__init__()

    def get_roles(self):
        return "INSTRUCTOR"

class Department:
    def __init__(self, dept_id, name):
        self.dept_id = dept_id
        self.name = name

        self.instructors = []
        self.courses = []

    def get_department(self, id)
        return ...

    def set_course(self, c):
        self.courses.append(c1)
        # save to database


class Course:
    def __init__(self, course_id, title )