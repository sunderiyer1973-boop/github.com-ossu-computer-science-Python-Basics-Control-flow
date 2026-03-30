import json
import os

# Student Details (as required)
STUDENT_NAME = "Sunder Iyer"
STUDENT_ID = "bitsom_ba_2511667"

FILE = "students.json"

# Load data from file
def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# Save data to file
def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

# Add student
def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    
    student = {
        "name": name,
        "marks": marks
    }
    
    data = load_data()
    data.append(student)
    save_data(data)
    
    print("✅ Student added successfully!")

# Grade calculation
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

# Show report
def show_report():
    data = load_data()
    
    if not data:
        print("No records found.")
        return
    
    print("\n===== Student Report =====")
    for s in data:
        grade = get_grade(s["marks"])
        print(f'{s["name"]} | Marks: {s["marks"]} | Grade: {grade}')

# Main menu
def menu():
    print("\n==============================")
    print(" Student Grade Tracker")
    print(" Developed by:", Sunder Iyer)
    print(" Student ID:", bitsom_ba_2511667)
    print("==============================")

    while True:
        print("\n1. Add Student")
        print("2. View Report")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            show_report()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

# Run program
if __name__ == "__main__":
    menu()
