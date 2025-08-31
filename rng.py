import random
import math

def getuserinput(x,y,attempts): #User gives their guess
    while True:
        try:
            # Get input and attempt to convert it to an integer
            user = int(input(f"\nYou have {attempts} attempts.\nEnter a number between {x} and {y}: "))

            # Check if the input is within the valid range
            if x <= user <= y:
                return user  # Return the valid number
            else:
                print(f"Out of range! Please enter a number between {x} and {y}.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def setrange(): #User sets range for random number generation
    while True:
        try:
            # Get user input for min and max
            x = int(input("Enter minimum number: "))
            y = int(input("Enter maximum number: "))

            # Check if min is less than or equal to max
            if x <= y:
                return x, y
            else:
                print("Invalid range! Minimum should be less than or equal to maximum.")
        except ValueError:
            print("Invalid input! Please enter valid numbers.")

def setdifficulty(options): #User decides difficulty
    while True:
        difficulty = input("\nChoose a difficulty:"
    "\n1.Easy\n"
    "2.Medium\n"
    "3.Hard\n"
    "4.Elite\n"
    "5.Master\n"
    "6.GrandMaster\n")
    
        if difficulty == "1":
            return math.ceil(options * 2)
        elif difficulty == "2":
            return math.ceil(options * 1)
        elif difficulty == "3":
            return math.ceil(options *0.8)
        elif difficulty == "4":
            return math.ceil(options * 0.50)
        elif difficulty == "5":
            return math.ceil(options * 0.40)
        elif difficulty == "6":
            return math.ceil(options * 0.05)
        else:
            print("Invalid Selection: Try Again")
    
def menu(): #starts the program
    while True:
        print("\n\n\nNumber Guessing Game")
        print     ("*********************")
        if input("'x' to exit, any other key to play:").lower().strip() == 'x': return
        else:
            (min,max) = setrange()
            correct = random.randint(min,max)
            attempts = setdifficulty(max-min+1)
            play(correct,min,max,attempts)



def play(correct,min,max,attempts): #Loops until player wins or loses
    while attempts >0:
        user = int(getuserinput(min,max,attempts))
        if user == correct:
            attempts -= 1
            print(f"\nYou Win! You had {attempts} attempts left.")
            break
        elif user > correct:
            attempts -= 1
            if attempts>0:
                print(f"Too High!")
            else:
                print(f"Sorry, You Lose. The correct answer was {correct}")
        elif user < correct:
            attempts -=1
            if attempts>0:
                print(f"Too Low!")
            else:
                print(f"Sorry, You Lose. The correct answer was {correct}")

def play_again():
    again = input("Play again? (y/n): ").lower()
    if again != "y":
        return False
    else:
        return True


if __name__ == "__main__":
    while menu():
        pass