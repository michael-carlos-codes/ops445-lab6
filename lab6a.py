#!/usr/bin/env python3
# Author ID: Michael Carlos

class Student:
    # Define the name and number when a student object is created
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)  # Ensure number is stored as a string
        self.courses = {}

    # Return student name and number
    def displayStudent(self):
        return f'Student Name: {self.name}\nStudent Number: {self.number}'

    # Add a new course and grade to student's record
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # Calculate the grade point average of all courses and return a string
    def displayGPA(self):
        if not self.courses:  # Prevent division by zero if no courses are added
            return f'GPA of student {self.name} is 0.0'  # This is the fixed output for no courses
        gpa = sum(self.courses.values()) / len(self.courses)
        return f'GPA of student {self.name} is {gpa:.1f}'  # GPA with 1 decimal place

    # Return a list of courses that the student passed (not a 0.0 grade)
    def displayCourses(self):
        passed_courses = [course for course, grade in self.courses.items() if grade > 0.0]
        return passed_courses

if __name__ == '__main__':
    # Create first student object and add grades for each class
    student1 = Student('John', 13454900)  # Integer student number test
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object and add grades for each class
    student2 = Student('Jessica', 123456)  # Integer student number test
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Create third student object (no grades, for GPA = 0.0 case)
    student3 = Student('Alice', 987654)

    # Display information for student1 object
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display information for student2 object
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())

    # Display information for student3 object (no courses)
    print(student3.displayStudent())
    print(student3.displayGPA())  # This should output GPA of student Alice is 0.0
    print(student3.displayCourses())  # This should output an empty list
