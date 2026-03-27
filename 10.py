def print_numbers_with_digits(A, B):
    """Prints in ascending order all numbers in the range A to B
    that consist only of the digits {1, 3, 4, 8, 9}"""
    
    if A > B:
        A, B = B, A

    allowed_digits = {'1', '3', '4', '8', '9'}
    
    for num in range(A, B + 1):
        num_str = str(num)

        valid = True
        for digit in num_str:
            if digit not in allowed_digits:
                valid = False
                break

        if valid:
            print(num, end=" ")
    
    print()

print_numbers_with_digits(50, 1)
