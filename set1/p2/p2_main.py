# Name:     Pacopac,Ace M.
# Section:  IV-BSIT A


import student_utils                                    
from student_utils import get_highest, get_lowest      
from datetime import datetime                          


def read_count():
    while True:
        try:
            count = int(input("How many subjects? "))
            if count >= 1:
                return count
            print("Enter at least 1.")
        except ValueError:
            print("Please enter a whole number.")


def read_grade(prompt):
    while True:
        try:
            grade = float(input(prompt))
            if 0 <= grade <= 100:
                return grade
            print("Grade must be from 0 to 100.")
        except ValueError:
            print("Please enter a number.")


def main():
    print("=== Student Grade Report - Your Name ===")
    count = read_count()
    grades = []
    for i in range(count):
        grades.append(read_grade(f"Grade for subject #{i + 1}: "))

    
    average = student_utils.compute_average(grades)
    status = student_utils.get_status(average)

    
    highest = get_highest(grades)
    lowest = get_lowest(grades)

    
    generated = datetime.now().strftime("%B %d, %Y %I:%M %p")

    print("\n----- GRADE REPORT -----")
    print(f"Generated: {generated}")
    print(f"Grades:    {grades}")
    print(f"Average:   {average:.2f}")
    print(f"Highest:   {highest}")
    print(f"Lowest:    {lowest}")
    print(f"Status:    {status}")


main()