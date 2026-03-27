def simple(n):
    """Checks if a number is prime"""
    
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def simple_to_N():
    """Prints all prime numbers from 1 to N"""
    
    N = int(input("Введите натуральное число N: "))
    
    print(f"Простые числа от 1 до {N}:")
    
    for i in range(1, N + 1):
        if simple(i):
            print(i, end=" ")
    
    print()

simple_to_N()
