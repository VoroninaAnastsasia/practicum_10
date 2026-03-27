def print_common_multiples(A, B, N):
    """The function displays in ascending order all
    common multiples of the numbers A and B that do not exceed N"""

    found = False
    
    for i in range(1, N + 1):
        if i % A == 0 and i % B == 0:
            print(i, end=" ")
            found = True
    
    if not found:
        print("Общих кратных нет")
        
print_common_multiples(7, 11, 50)
