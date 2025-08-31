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
    if not nums:
        print("Cannot sort empty list")
        return []

    sorted_nums = [nums.pop(0)]
    steps = 0

    while nums:
        inserted = False
        current = nums[0]

        for i in range(len(sorted_nums)):
            if current < sorted_nums[i]:
                sorted_nums.insert(i, nums.pop(0))
                steps += 1
                highlighted = "[ " + " , ".join(
                    f"{BLUE}{v}{RESET}" if idx == i else str(v)
                    for idx, v in enumerate(sorted_nums)
                ) + " ]"
                divider = "-" * (len(nums) + len(sorted_nums))
                print(f"{highlighted}")
                inserted = True
                break

        if not inserted:
            sorted_nums.append(nums.pop(0))
            steps += 1
            last_idx = len(sorted_nums) - 1
            highlighted = "[ " + " , ".join(
                f"{BLUE}{v}{RESET}" if idx == last_idx else str(v)
                for idx, v in enumerate(sorted_nums)
            ) + " ]"
            print(f"{highlighted}")

    print(f"Final Results: {sorted_nums}\nSteps Taken: {steps}")
    return sorted_nums

 
def selection_sort():
    nums = get_nums()
    
    for fix_idx in range(len(nums)):
        min_idx = fix_idx
        for check_idx in range(fix_idx+1,(len(nums))):
            if nums[check_idx] < nums[min_idx]: 
                min_idx = check_idx    #find lowest in unsorted                           
        
        nums[fix_idx],nums[min_idx] =nums[min_idx],nums[fix_idx]    #swap fix with min
        print("[ " + " , ".join(f"{BLUE}{val}{RESET}" if idx == fix_idx else str(val)for idx, val in enumerate(nums)) + " ]"
)

            



def menu():
    header = "    sorting.py Menu     "
    print(f"{header}\n{'-'*len(header)}")
    
    menu_choice = input(
"""Make a Selection:
1.Bubble Sort
2.Insertion Sort
3.Selection Sort
x.exit
""")
    
    match menu_choice.lower():
        case '1':
            bubble_sort()
        case '2':
            insertion_sort()
        case '3':
            selection_sort()
        case 'x':
            return False
        case _:
            print("Invalid choice")
    
    return True

    
if __name__ == "__main__":
    while menu():
        pass