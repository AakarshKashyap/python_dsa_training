class Student:
    def __init__(self, id, name, marks):
        self.id = id
        self.name = name
        self.marks = marks
        self.next = None

class Students:
    def __init__(self):
        self.head = None

    def register_student_at_beginning(self, id, name, marks):
        new_student = Student(id, name, marks)

        if self.head is None:
            self.head = new_student
            print("Student registered successfully!\n")
            return
        
        new_student.next = self.head
        self.head = new_student
        
        print("Student registered successfully!\n")

    def register_student_at_end(self, id, name, marks):
        new_student = Student(id, name, marks)

        if self.head is None:
            self.head = new_student
            print("Student registered successfully!\n")
            return
    
        temp = self.head
    
        while temp.next is not None:
            temp = temp.next
    
        temp.next = new_student
    
        print("Student registered successfully!\n")

    def register_student_at_position(self, id, name, marks, pos):
        if pos <= 0:
            print("Invalid position!\n")
            return
    
        if pos == 1:
            self.register_student_at_beginning(id, name, marks)
            return
    
        new_student = Student(id, name, marks)
    
        i = 1
        temp = self.head
    
        while i < pos - 1 and temp is not None:
            temp = temp.next
            i += 1
    
        if temp is None:
            print("Students are less than the specified position!\n")
            return
    
        new_student.next = temp.next
        temp.next = new_student
    
        print("Student registered successfully!\n")

    def search_student_by_id(self, id):
        if self.head is None:
            return "No students in the records!"

        temp = self.head
        pos = 1

        while temp is not None:
            if temp.id == id:
                return f"Student with id {id} found at position {pos}"

            temp = temp.next
            pos += 1

        return f"Student with id {id} not found in the records!"

    def remove_student_by_id(self, id):
        if self.head is None:
            print("No students in the records!\n")
            return

        if self.head.id == id:
            self.head = self.head.next
            print(f"Student with id {id} removed successfully\n")
            return

        temp = self.head
        prev = None

        while temp is not None:
            if temp.id == id:
                prev.next = temp.next
                print(f"Student with id {id} removed successfully!\n")
                return

            prev = temp
            temp = temp.next

        print(f"Student with id {id} not found in the records!")

    def display_students_in_records(self):
        if self.head is None:
            print("No students in the records!\n")
            return

        temp = self.head

        print("Students:")
        while temp is not None:
            print(f"ID: {temp.id} | Name: {temp.name} | Marks: {temp.marks}")
            temp = temp.next

        print()

    def get_number_of_students(self):
        if self.head is None:
            return 0

        length = 1
        temp = self.head

        while temp.next is not None:
            temp = temp.next
            length += 1

        return length

    def get_student_with_highest_marks(self):
        if self.head is None:
            print("No students in the records!\n")
            return

        if self.head.next is None:
            print(f"ID of student with highest marks: {self.head.id}\n")
            return

        highest = self.head.marks
        student_with_highest_marks = self.head

        temp = self.head

        while temp is not None:
            if temp.marks > highest:
                highest = temp.marks
                student_with_highest_marks = temp

            temp = temp.next

        print("Student with highest marks:")
        print(f"ID: {student_with_highest_marks.id}")
        print(f"Name: {student_with_highest_marks.name}")
        print(f"Marks: {student_with_highest_marks.marks}\n")

    def reverse_registration_records(self):
        if self.head is None:
            print("No students in the records!\n")
            return

        if self.head.next is None:
            print("Only one student in the records!\n")
            return

        prev = None
        curr = self.head

        while curr is not None:
            temp = curr.next

            curr.next = prev
            prev = curr
            curr=temp

        self.head = prev

        print("Registration records reversed successfully!\n")

students = Students()

print("\n================================")
print("STUDENT REGISTRATION RECORDS")
print("================================\n")

while True:
    print("Menu:")
    print("1. Register a student at the beginning")
    print("2. Register a student at the end")
    print("3. Register a student at a specified position")
    print("4. Remove a student using the Student ID")
    print("5. Search for a student using the Student ID")
    print("6. Display all registered students")
    print("7. Display the total number of registered students")
    print("8. Find and display the student who has the highest marks")
    print("9. Reverse the registration order")
    print("10. Exit the application")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            id = int(input("Enter your ID: "))
            name = input("Enter your name: ")
            marks = int(input("Enter your marks: "))
            students.register_student_at_beginning(id, name, marks)

        case 2:
            id = int(input("Enter your ID: "))
            name = input("Enter your name: ")
            marks = int(input("Enter your marks: "))
            students.register_student_at_end(id, name, marks)

        case 3:
            id = int(input("Enter your ID: "))
            name = input("Enter your name: ")
            marks = int(input("Enter your marks: "))
            position = int(input("Enter position of student where you want to register: "))
            students.register_student_at_position(id, name, marks, position)

        case 4:
            id = int(input("Enter ID of student to remove: "))
            students.remove_student_by_id(id)

        case 5:
            id = int(input("Enter ID of student to search: "))
            print(students.search_student_by_id(id))

        case 6:
            students.display_students_in_records()

        case 7:
            print(f"Total students in the records: {students.get_number_of_students()}")

        case 8:
            students.get_student_with_highest_marks()

        case 9:
            students.reverse_registration_records()

        case 10:
            print("\nApplication exited successfully!")
            break