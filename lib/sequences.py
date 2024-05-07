#!/usr/bin/env python3

def print_fibonacci(length):
    if(length == 0):
        return print([])
    elif(length == 1):
        return print([0])
    elif(length == 2):
        return print([0,1])
    elif length >= 10:
        fibonacci_sequence = [0, 1] 
        for i in range(2, length):
            next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_fibonacci)

            if len(fibonacci_sequence) == length:
                return print(fibonacci_sequence)
        
        return print(fibonacci_sequence)

    
