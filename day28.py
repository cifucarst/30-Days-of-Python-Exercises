#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    nList = []
    pattern = '@gmail\.com'
    regex = re.compile(pattern)
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        
        if regex.search(emailID):
            nList.append(firstName)
    nList.sort()   
    for name in nList:
        print(name)
