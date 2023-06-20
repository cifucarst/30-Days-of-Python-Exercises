# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def isPrime(n):
    if n <= 1:
        return False
    sqrt_n = math.sqrt(n)
    if sqrt_n.is_integer():
        return False
    for idx in range(2, int(sqrt_n) + 1):
        if n % idx == 0:
            return False
    return True
        
num = int(input())
for idx in range(num):
    n = int(input())
    if isPrime(n):
        print("Prime")
    else:
        print("Not prime")