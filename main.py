import sorting
import rng

def menu():
    header = "     Menu     "
    print(f"{header}\n{'-'*len(header)}")
    
    menu_choice = input(
"""Make a Selection:
1.Sorting
2.Number Guessing Game
x.exit
""")
    
    match menu_choice.lower().strip():
        case '1':
            sorting.menu()
        case '2':
            rng.menu()
        case 'x':
            return False
        case _:
            print("Invalid choice")
    
    return True

while menu():
    menu()