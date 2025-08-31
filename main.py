import sorting

def menu():
    header = "     Menu     "
    print(f"{header}\n{'-'*len(header)}")
    
    menu_choice = input(
"""Make a Selection:
1.Sorting
x.exit
""")
    
    match menu_choice.lower():
        case '1':
            sorting.menu()
        case 'x':
            return False
        case _:
            print("Invalid choice")
    
    return True

while menu():
    menu()