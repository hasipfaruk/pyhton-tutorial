
# Test Code is here
class SoftwareEngineeringDept:
    def __init__(self):
        self.students = {}  # Dictionary to store student records
        self.menu()

    def menu(self):
        userinput = input("""
        Welcome to the Software Engineering Department:
        Please select an option for further process:
        1. Register a student
        2. View student's data
        3. Update student details
        4. Delete student record
        5. Exit
        Select an option: """).strip()

        if userinput == "1":
            self.register_stu()
        elif userinput == "2":
            self.view_stu()
        elif userinput == "3":
            self.update_stu()
        elif userinput == "4":
            self.del_stu()
        elif userinput == "5":
            print("Thank you! Exiting...")
            exit()
        else:
            print("⚠ Alert: Invalid option, please select a valid option.")

        self.menu()  # Keep displaying the menu until the user exits

    def register_stu(self):
        stu_id = input("Enter student ID: ").strip()
        if stu_id in self.students:
            print("⚠ Student already exists!")
        else:
            name = input("Enter student name: ").strip()
            year = input("Enter year of study: ").strip()
            self.students[stu_id] = {"name": name, "year": year}
            print("✅ Student registered successfully!")
        self.menu()

    def view_stu(self):
        stu_id = input("Enter student ID: ").strip()
        if stu_id in self.students:
            print("📄 Student Details:")
            print(f"ID: {stu_id}, Name: {self.students[stu_id]['name']}, Year: {self.students[stu_id]['year']}")
        else:
            print("⚠ Student ID not found!")
        self.menu()

    def update_stu(self):
        stu_id = input("Enter the student ID you want to update: ").strip()
        if stu_id in self.students:
            name = input("Enter new name: ").strip()
            year = input("Enter new year of study: ").strip()
            self.students[stu_id] = {"name": name, "year": year}
            print("✅ Student details updated successfully!")
        else:
            print("⚠ Student ID not found!")
        self.menu()

    def del_stu(self):
        stu_id = input("Enter the student ID you want to delete: ").strip()
        if stu_id in self.students:
            del self.students[stu_id]
            print("✅ Student record deleted successfully!")
        else:
            print("⚠ Student ID not found!")
        self.menu()


# Create an instance of the class
obj = SoftwareEngineeringDept()
