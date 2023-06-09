#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#

def bitwiseAnd(N, K):
    # Initialize the maximum bitwise AND value.
    max_and = 0

    # Iterate through all possible pairs of integers from 1 to N.
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            # Calculate the bitwise AND of the two integers.
            current_and = i & j

            # If the bitwise AND is greater than the maximum value so far,
            # update the maximum value.
            if current_and > max_and and current_and < K:
                max_and = current_and

    # Return the maximum bitwise AND value.
    return max_and

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()
