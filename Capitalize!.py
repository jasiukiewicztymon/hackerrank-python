#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    spt = s.split(' ')
    out = ''
    for i in spt:
        for _ in range(len(i)):
            if (_ == 0):
                out += i[_].upper()
            else:
                out += i[_]
        out += ' '
    
    return out
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
