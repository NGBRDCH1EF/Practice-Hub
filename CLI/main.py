import sorting
import rng
import first
import anagram
import palindrome
import prime_numbers

def menu():
    header = "     Menu     "
    print(f"{header}\n{'-'*len(header)}")
    
    menu_choice = input(
"""Make a Selection:
1.Sorting
2.Number Guessing Game
3.My first script
4.Anagrams
5.Palindromes
6.Prime numbers
x.exit
""")
    
    match menu_choice.lower().strip():
        case '1':
            sorting.menu()
        case '2':
            rng.menu()
        case '3':
            first.menu()
        case '4':
            anagram.menu()
        case '5':
            palindrome.menu()
        case '6':
            prime_numbers.menu()
        case 'x':
            return False
        case _:
            print("Invalid choice")
    
    return True

while menu():
    menu()