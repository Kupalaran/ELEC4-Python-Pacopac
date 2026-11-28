# Name:     Pacopac,Ace M.
# Section:  IV-BSIT A



def divide_numbers():
    try:
        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))
        result = first / second
    except ValueError:                 # show if input was not a number
        print("Error: please enter numbers only.")
    except ZeroDivisionError:          # second number was 0
        print("Error: cannot divide by zero.")
    else:                              
        print(f"Result: {first} / {second} = {result:.2f}")
    finally:                           
        print("Division finished.")


def open_file():
    file_name = input("Enter file name: ").strip()
    try:
        with open(file_name, "r") as file:
            contents = file.read()
    except FileNotFoundError:         
        print(f"Error: '{file_name}' was not found.")
    else:
        print(f"\n--- {file_name} ---")
        print(contents)
    finally:
        print("File option finished.")


def main():
    while True:
        print("\n=== Safe Menu Program ===")
        print("[1] Divide two numbers")
        print("[2] Open a file")
        print("[3] Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            divide_numbers()
        elif choice == "2":
            open_file()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.")


main()