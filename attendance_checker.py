
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

    total = len(students)

    print("\n===== ATTENDANCE SUMMARY =====")
    print(f"Total students: {total}")
    print(f"Present: {present}")
    print(f"Absent: {absent}")
    print(f"Not marked: {not_marked}")

    if total > 0:
        percentage = (present / total) * 100
        print(f"Attendance percentage: {percentage:.2f}%")
    else:
        print("No students registered yet.")


