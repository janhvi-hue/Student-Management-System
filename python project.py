#----- STUDENT MANAGEMENT SYSTEM -----#

Students = [
  {"id": "1", "name": "Janhvi", "marks": [80, 85, 90]},
  {"id": "2", "name": "Rahul", "marks": [70, 75, 78]}
]

import json

students = []

# ---------------- FUNCTIONS ---------------- #

def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    marks = list(map(int, input("Enter marks (space separated): ").split()))
    
    for s in students:
        if s["id"] == sid:
            print("ID already exist")
            return
    
    student = {
        "id": sid,
        "name": name,
        "marks": marks
    }
    
    students.append(student)
    print("Student added successfully!\n")


def view_students():
    if not students:
        print("No records found.\n")
        return
    
    #for s in students:
        #print(f"ID: {s['id']}, Name: {s['name']}, Marks: {s['marks']}")
    #print()

    for s in students:
        avg = sum(s["marks"]) / len(s["marks"])
        print(f"ID: {s['id']}, Name: {s['name']}, Marks: {s['marks']}, Avg: {avg:.2f}")
    
    for s in students:
        if avg >=90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 50:
            grade = "C"
        else:
            grade = "F"
        print(f"ID: {s['id']}, Name: {s['name']}, Marks: {s['marks']}, Avg: {avg:.2f}, Grade: {grade}")


def search_student():
    sid = input("Enter Student ID to search: ")
    
    for s in students:
        if s["id"] == sid:
            print(s)
            return
    
    print("Student not found.\n")

def update_student():
        sid = input("Enter Student ID to update: ")

        for s in students:
            if s["id"] == sid:
                print("student found!\n")
                new_name = input("enter name: ")
                new_marks = list(map(int,input("enter marks: ").split()))

                s["name"] = new_name
                s["marks"] = new_marks
                print("Updated successfully!\n")
                return
        print("student not found\n")
    


def delete_student():
    sid = input("Enter Student ID to delete: ")
    
    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("Deleted successfully!\n")
            return
    
    print("Student not found.\n")


def save_data():
    with open("students.json", "w") as f:
        json.dump(students, f)
    print("Data saved!\n")


def load_data():
    global students
    try:
        with open("students.json", "r") as f:
            students = json.load(f)
    except FileNotFoundError:
        students = []
    print("Loaded:", students)

# ---------------- MAIN PROGRAM ---------------- #

load_data()

while True:
    print("---- Student Management System ----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Save Data")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        save_data()
    elif choice == "7":
        save_data()
        print("Exiting...")
        break
    else:
        print("Invalid choice!\n")