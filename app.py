student_list = []
# Now integrating to Git

class Student(object):

    def __init__(self, name):
        self.name = name
        self.marks = []


def create_student():
    name = input("Please enter the student's name: ")
    return Student(name)


def append_mark(student, mark):
    student.marks.append(mark)


def calculate_average_mark(student):
    divisor = len(student.marks)
    if divisor == 0:
        return 0
    suma = sum(student.marks)
    return suma / divisor


def print_student_details(student):
    print("student's name ", student.name)
    print("student's average ", calculate_average_mark(student))


def print_student_list(students):
    for i, student in enumerate(students):
        print("ID: {}".format(i))
        print_student_details(student)


def menu():
    selection = input("Enter 'p' to print the student's list, "
                      "'s' to add a new student, "
                      "'a' to add a mark to a student, or "
                      "'q' to quit: ")
    while selection != 'q':

        if selection == 'p':
            print_student_list(student_list)
        elif selection == 's':
            student = create_student()
            student_list.append(student)
        elif selection == 'a':
            print_student_list(student_list)
            student_id = int(input("enter the student ID to add a mark to: "))
            student = student_list[student_id]
            mark = int(input("Enter the new mark to be added: "))
            append_mark(student, mark)

        selection = input("Enter 'p' to print the student's list, "
                          "'s' to add a new student, "
                          "'a' to add a mark to a student, or "
                          "'q' to quit ")


menu()
