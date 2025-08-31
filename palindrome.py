def menu():

    word = input("Enter a word: \n").lower()
    cleaned_word = word.replace(" ","")
    backwards =""

    for char in range(len(cleaned_word)-1,-1,-1):
        backwards += (cleaned_word[char])

    if backwards == cleaned_word:
        print(f"Yes, \"{backwards}\" is a palindrome!")
    else: 
        print(f"No, \"{word}\" is not a palindrome.")

if __name__ == "__main__":
    while menu():
        pass