"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError
    
    list = [2]
    num = 3
    
    while len(list) < number_of_primes:
        isPrime = True
        for i in range(2, num):
            if num % i == 0:
                isPrime = False
        if isPrime:
            list.append(num) 
        num += 1       
    return list
