BLUE = "\033[94m"   # ANSI code for bright blue
GREEN = "\033[92m"  # ANSI code for green
RESET = "\033[0m"   # Reset to default color


def get_nums() -> list:
    nums = []
    while not nums:
        
        raw = input("Enter nums seperated by commas: ")
        
        for num in raw.split(","):
            num = num.strip()
            if not num:
                pass
            else:
                try:
                    nums.append(int(num))
                except ValueError:
                    print(f"Ignorning invalid entry: {num}")
        if nums: return nums

    
def bubble_sort() -> list:
    nums = get_nums()
    n = len(nums)


    steps=0
    for _ in range(n):
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                a, b = nums[i], nums[i+1]
                nums[i], nums[i+1] = b, a
                
                highlighted = [
                    f"{BLUE}{x}{RESET}" if x in (a, b) and idx in (i, i+1) else str(x)
                    for idx, x in enumerate(nums)
                ]

                print(" , ".join(highlighted))
                steps += 1
    print(f"{GREEN}Final Results: {nums}\nSteps Taken: {steps}{RESET}")

    return nums
    
def insertion_sort():
    nums = get_nums()
    sorted_nums = []
    sorted_nums.append(nums.pop(0))
    steps = 0
    while nums:
        inserted = False
        for i in range(len(sorted_nums)):
            if nums[0] < sorted_nums[i]:
                sorted_nums.insert(i,nums.pop(0))
                inserted = True
                steps += 1
                break
        if not inserted:
            sorted_nums.append(nums.pop(0))
            steps += 1 
        if len(nums)>0:
            print(f"{sorted_nums}<{"-"*(len(nums)+len(sorted_nums))}{nums}")

    print(f"{GREEN}Final Results: {sorted_nums}\nSteps Taken: {steps}{RESET}")

    return sorted_nums

            


def menu():
    header = "     Menu     "
    print(f"{header}\n{'-'*len(header)}")
    
    menu_choice = input(
"""Make a Selection:
1.Bubble Sort
2.Insertion Sort
x.exit
""")
    
    match menu_choice.lower():
        case '1':
            bubble_sort()
        case '2':
            insertion_sort()
        case 'x':
            return False
        case _:
            print("Invalid choice")
    
    return True

    
while menu():
    menu()