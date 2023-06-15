#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    totalSwaps = 0
    for i in range(n):
        swaps = 0
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                swaps += 1
        totalSwaps += swaps
            
        if swaps == 0:
            break
    
    print(f'Array is sorted in {totalSwaps} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[n - 1]}')