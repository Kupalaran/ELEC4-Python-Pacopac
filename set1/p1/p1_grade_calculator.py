# Name:     Paopac,Ace M.
# Section:  IV-BSIT A
# Activity: P1 - Student Grade Calculator
# Date:     2026-11-21

PASSING_AVERAGE = 75   


# the computing functions

def compute_average(grades):
    return sum(grades) / len(grades)


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)


def get_status(average, passing=PASSING_AVERAGE):
    
    return "PASSED" if average >= passing else "FAILED"


# this are input functions

def read_count():
    while True:
        try:
            count = int(input("How many subjects? "))
            if count >= 1:
                return count
            print("Enter at least 1.")
        except ValueError:          # e.g. "abc" or "2.5"
            print("Please enter a whole number.")


def read_grade(prompt):
    while True:
        try:
            grade = float(input(prompt))
            if 0 <= grade <= 100:
                return grade        # loop if not in 0 - 100 range
            print("Grade must be from 0 to 100.")
        except ValueError:          # if input not number
            print("Please enter a number.")


def input_grades():
    count = read_count()
    grades = []                  
    for i in range(count):
        grades.append(read_grade(f"Grade for subject #{i + 1}: "))
    return grades


# Output 

def show_results(grades):
    average = compute_average(grades)   
    print(f"\nGrades:  {grades}")
    print(f"Average: {average:.2f}")
    print(f"Highest: {get_highest(grades)}")
    print(f"Lowest:  {get_lowest(grades)}")
    print(f"Status:  {get_status(average)}")


# Menu 

def main():
    grades = []                    
    while True:
        print("\n=== Student Grade Calculator ===")
        print("[1] Enter grades")
        print("[2] View results")
        print("[3] Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            grades = input_grades()
            show_results(grades)    
        elif choice == "2":
            if not grades:          
                print("No grades yet. Choose 1 first.")
            else:
                show_results(grades)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.")


main()


# Local vs. global variables:
# the global variable(passing_average) is created outside of all functions
# so every functions can read it, which is why get_status can use it.
# the local variable is created inside a function and can onle be used inside that function.