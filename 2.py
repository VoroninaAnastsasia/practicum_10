def print_fibonacci(n):
    """The function prints the first N numbers of the Fibonacci sequence"""
    
    if n <= 0:
        return
    
    if n == 1:
        print(1)
        return
    
    a, b = 1, 1
    print(a, end=" ")
    print(b, end=" ")
    
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c
    
    print()

print_fibonacci()
