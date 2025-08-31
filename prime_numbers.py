import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def menu():
    print("\nPrime Number Generator")
    choice = input("Press Enter to show 50 primes, or 'x' to exit: ").lower().strip()

    if choice == "x":
        return False

    # generate primes
    i = 2
    count = 0
    while count < 50:
        if is_prime(i):
            count += 1
            print(f"{count}. {i}")
        i += 1
    return True   # keep looping unless user chose 'x'


if __name__ == "__main__":
    while menu():
        pass

