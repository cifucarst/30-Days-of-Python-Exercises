import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    
    maxcounter = 0
    counter = 0
    
    while n > 0:
        remainder = n % 2
        if remainder == 1:
            counter += 1
            maxcounter = max(maxcounter, counter)
        else:
            counter = 0
        n = n // 2
    
    print(maxcounter)