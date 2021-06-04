#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # li = []
    # for i in range(len(arr)):
    #     if i+1 > len(arr)-1:
    #         break
    #     for j in range(i+1, len(arr)):
    #         li.append(abs(arr[i]-arr[j]))
    # return min(li)
    arr = sorted(arr)
    tmp = abs(arr[1]-arr[0])
    for i in range(1, len(arr)-1):
        n_tmp = abs(arr[i+1]-arr[i])
        if tmp >= n_tmp:
            tmp = n_tmp
    return tmp
            
            
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
