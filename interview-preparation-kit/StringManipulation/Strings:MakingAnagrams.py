#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    ct_a = Counter(a)
    ct_b = Counter(b)
    ct_a.subtract(ct_b)
    return sum(abs(i) for i in ct_a.values())
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
