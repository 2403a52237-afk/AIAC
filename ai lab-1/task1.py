class SRUStudent:
    def __init__(self, name, roll_no, department):
        self.name = name
        self.roll_no = roll_no
        self.department = department

    def student_data(self):
        # Store details in a text document
        filename = f"{self.roll_no}_student.txt"
        with open(filename, "w") as file:
            file.write(f"Name: {self.name}\n")
            file.write(f"Roll No: {self.roll_no}\n")
            file.write(f"Department: {self.department}\n")
        # Show student details
        print("Student Details:")
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Department: {self.department}")

# Example usage
if __name__ == "__main__":
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    department = input("Enter department: ")
    student = SRUStudent(name, roll_no, department)
    student.student_data()