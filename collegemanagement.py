#College Management System Project

class Student:  
    def __init__(self, student_id, name, age, course):  
        self.student_id = student_id  
        self.name = name  
        self.age = age  
        self.course = course  

    def __str__(self):  
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Course: {self.course}"  


class Course:  
    def __init__(self, course_id, course_name, duration):  
        self.course_id = course_id  
        self.course_name = course_name  
        self.duration = duration  

    def __str__(self):  
        return f"Course ID: {self.course_id}, Course Name: {self.course_name}, Duration: {self.duration} months"  


class Faculty:  
    def __init__(self, faculty_id, name, subject):  
        self.faculty_id = faculty_id  
        self.name = name  
        self.subject = subject  

    def __str__(self):  
        return f"Faculty ID: {self.faculty_id}, Name: {self.name}, Subject: {self.subject}"  


class CollegeManagementSystem:  
    def __init__(self):  
        self.students = []  
        self.courses = []  
        self.faculties = []  

    def add_student(self, student_id, name, age, course):  
        new_student = Student(student_id, name, age, course)  
        self.students.append(new_student)  
        print(f"Student {name} added successfully.")  

    def view_students(self):  
        for student in self.students:  
            print(student)  

    def update_student(self, student_id, name=None, age=None, course=None):  
        for student in self.students:  
            if student.student_id == student_id:  
                if name:  
                    student.name = name  
                if age:  
                    student.age = age  
                if course:  
                    student.course = course  
                print(f"Student ID {student_id} updated successfully.")  
                return  
        print("Student not found.")  

    def delete_student(self, student_id):  
        for student in self.students:  
            if student.student_id == student_id:  
                self.students.remove(student)  
                print(f"Student ID {student_id} deleted successfully.")  
                return  
        print("Student not found.")  

    def add_course(self, course_id, course_name, duration):  
        new_course = Course(course_id, course_name, duration)  
        self.courses.append(new_course)  
        print(f"Course {course_name} added successfully.")  

    def view_courses(self):  
        for course in self.courses:  
            print(course)  

    def add_faculty(self, faculty_id, name, subject):  
        new_faculty = Faculty(faculty_id, name, subject)  
        self.faculties.append(new_faculty)  
        print(f"Faculty {name} added successfully.")  

    def view_faculties(self):  
        for faculty in self.faculties:  
            print(faculty)  


def main():  
    cms = CollegeManagementSystem()  
    
    while True:  
        print("\nCollege Management System")  
        print("1. Add Student")  
        print("2. View Students")  
        print("3. Update Student")  
        print("4. Delete Student")  
        print("5. Add Course")  
        print("6. View Courses")  
        print("7. Add Faculty")  
        print("8. View Faculties")  
        print("9. Exit")  
        
        choice = input("Choose an option: ")  

        if choice == '1':  
            student_id = input("Enter Student ID: ")  
            name = input("Enter Name: ")  
            age = int(input("Enter Age: "))  
            course = input("Enter Course: ")  
            cms.add_student(student_id, name, age, course)  
        
        elif choice == '2':  
            cms.view_students()  

        elif choice == '3':  
            student_id = input("Enter Student ID to update: ")  
            name = input("Enter new Name (leave blank to retain current): ")  
            age = input("Enter new Age (leave blank to retain current): ")  
            course = input("Enter new Course (leave blank to retain current): ")  
            cms.update_student(student_id, name if name else None,   
                               int(age) if age else None,  
                               course if course else None)  

        elif choice == '4':  
            student_id = input("Enter Student ID to delete: ")  
            cms.delete_student(student_id)  

        elif choice == '5':  
            course_id = input("Enter Course ID: ")  
            course_name = input("Enter Course Name: ")  
            duration = int(input("Enter Duration (in months): "))  
            cms.add_course(course_id, course_name, duration)  

        elif choice == '6':  
            cms.view_courses()  

        elif choice == '7':  
            faculty_id = input("Enter Faculty ID: ")  
            name = input("Enter Name: ")  
            subject = input("Enter Subject: ")  
            cms.add_faculty(faculty_id, name, subject)  

        elif choice == '8':  
            cms.view_faculties()  

        elif choice == '9':  
            print("Exiting the College Management System.")  
            break  
        
        else:  
            print("Invalid choice. Please try again.")  

if __name__ == "__main__":  
    main()
