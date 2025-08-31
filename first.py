def menu():
    while True:
        choose_function = input(
"""Choose a function:
 1. greet
 2. sum and product
 3. difference and quotient
 x. exit
> """
        ).lower().strip()

        match choose_function:
            case '1':
                greet()
            case '2':
                add_multiply()
            case '3':
                subtract_divide()
            case 'x':
                return   # exit the menu loop
            case _:
                print("Invalid Selection")

        pause()  # wait before showing the menu again

def greet():
    first = input("First Name:")
    last  = input("Last Name:")
    print(f"Hello {first.title()} {last.title()} ")
    print (f"{first} {last} contains {count_letters(first,last)} characters :D")


def count_letters(first,last):
    total_letters = len(first) + len(last)
    return total_letters

def add_multiply():
    num1 = int(input(" First Number:"))
    num2 = int(input("Second Number:"))
    print(f"Sum:{num1+num2}\nProduct:{num1*num2}\n")

def subtract_divide():
    num1 = int(input(" First Number:"))
    num2 = int(input("Second Number:"))
    print(f"Sum:{num1-num2}\nProduct:{num1/num2}\n")

def pause():
    input("Press Enter to continue...")

if __name__ == "__main__":
    while menu():
        pass