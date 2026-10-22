
students = {}


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
    elif name in students:
        print("Student is already registered.")
    else:
        students[name] = "Not Marked"
        print(f"{name} added successfully!")


def mark_attendance():
    if not students:
        print("No students registered yet.")
        return

    name = input("Enter student name: ").strip()

    if name not in students:
        print("Student not found. Add the student first.")
        return

    print("1. Present")
    print("2. Absent")
    choice = input("Choose attendance status: ").strip()

    if choice == "1":
        students[name] = "Present"
        print(f"{name} marked as Present.")
    elif choice == "2":
        students[name] = "Absent"
        print(f"{name} marked as Absent.")
    else:
        print("Invalid choice.")


def view_attendance():
    if not students:
        print("No students registered yet.")
        return

    print("\n===== ATTENDANCE RECORDS =====")
    for name, status in students.items():
        print(f"{name}: {status}")


def attendance_summary():
    present = sum(
        status == "Present" for status in students.values()
    )
    absent = sum(
        status == "Absent" for status in students.values()
    )
    not_marked = sum(
        status == "Not Marked" for status in students.values()
    )

    print("\n===== ATTENDANCE SUMMARY =====")
    print(f"Total students: {len(students)}")
    print(f"Present: {present}")
    print(f"Absent: {absent}")
    print(f"Not marked: {not_marked}")


def main():
    while True:
        print("\n===== STUDENT ATTENDANCE CHECKER =====")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. View Attendance Summary")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            view_attendance()
        elif choice == "4":
            attendance_summary()
        elif choice == "5":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()
