# Name:     Pacopac,Ace M.
# Section:  IV-BSIT A


# add function
def add_student(students, name_keys):
    name = input("Enter student name: ").strip()
    if name == "":
        print("Name cannot be blank.")
        return
    key = name.lower()                 
    if key in name_keys:
        print(f"'{name}' is already in the list.")
    else:
        students.append(name)
        name_keys.add(key)
        print(f"'{name}' added.")

#remove function
def remove_student(students, name_keys):
    name = input("Enter name to remove: ").strip()
    key = name.lower()
    if key not in name_keys:
        print(f"'{name}' was not found.")
        return
    for student in students:
        if student.lower() == key:
            students.remove(student)   
            break
    name_keys.remove(key)              
    print(f"'{name}' removed.")

#search function
def search_students(students):
    query = input("Search name: ").strip().lower()
    matches = [s for s in students if query in s.lower()]  
    if matches:
        print(f"Found {len(matches)} match(es):")
        for name in matches:
            print(f"  - {name}")
    else:
        print("No matching students.")

#display function
def display_students(students):
    if not students:
        print("No students yet.")
        return
    print("\n--- Student List ---")
    for number, name in enumerate(sorted(students, key=str.lower), start=1):
        print(f"{number}. {name}")
    print(f"Total students: {len(students)}")

#menu of the program
def main():
    students = []
    name_keys = set()
    while True:
        print("\n=== Student Record Manager ===")
        print("[1] Add student")
        print("[2] Remove student")
        print("[3] Search student")
        print("[4] Display all students")
        print("[5] Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            add_student(students, name_keys)
        elif choice == "2":
            remove_student(students, name_keys)
        elif choice == "3":
            search_students(students)
        elif choice == "4":
            display_students(students)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1 to 5.")


main()


# List vs. set:
#  a list keeps names in order and allows duplicates, 
#  supporting sorting, numbering, and search.
#  a set stores lowercase names for fast duplicate checks ex: "juan cruz".