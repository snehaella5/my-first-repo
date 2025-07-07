import csv
import os

STUDENT_FILE = "students.csv"

# Ensure the file exists
if not os.path.exists(STUDENT_FILE):
    with open(STUDENT_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Math", "Science", "English"])  # Header row

def add_student():
    name = input(" Enter student name: ")
    try:
        math = float(input(" Math grade: "))
        science = float(input(" Science grade: "))
        english = float(input(" English grade: "))
    except ValueError:
        print(" Invalid grade entered. Try again.")
        return

    with open(STUDENT_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, math, science, english])
    print("Student added successfully!")

def view_students():
    print("\n All Students:")
    with open(STUDENT_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(" | ".join(row))

def search_student():
    name_to_find = input(" Enter name to search: ").lower()
    found = False
    with open(STUDENT_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].lower() == name_to_find:
                print(" Student Found: ", row)
                found = True
                break
    if not found:
        print(" Student not found.")

def calculate_averages():
    total = 0
    count = 0
    with open(STUDENT_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            grades = list(map(float, row[1:]))
            total += sum(grades) / len(grades)
            count += 1
    if count > 0:
        print(f" Class Average Grade: {round(total / count, 2)}")
    else:
        print(" No students in the system yet.")

def menu():
    while True:
        print("\n GradeMaster - Student Grade Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Name")
        print("4. Calculate Class Average")
        print("5. Exit")

        choice = input(" Enter your choice (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            calculate_averages()
        elif choice == '5':
            print(" Exiting GradeMaster. Goodbye!")
            break
        else:
            print(" Invalid choice. Please select between 1 and 5.")

if __name__ == "__main__":
    menu()
