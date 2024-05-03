# Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

# The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).

# The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].

# If a[i] > b[i], then Alice is awarded 1 point.
# If a[i] < b[i], then Bob is awarded 1 point.
# If a[i] = b[i], then neither person receives a point.
# Comparison points is the total points a person earned.

# Given a and b, determine their respective comparison points.

# Example

# a = [1, 2, 3]
# b = [3, 2, 1]
# For elements *0*, Bob is awarded a point because a[0] .
# For the equal elements a[1] and b[1], no points are earned.
# Finally, for elements 2, a[2] > b[2] so Alice receives a point.
# The return array is [1, 1] with Alice's score first and Bob's second.

# Function Description

# Complete the function compareTriplets in the editor below.

# compareTriplets has the following parameter(s):

# int a[3]: Alice's challenge rating
# int b[3]: Bob's challenge rating
# Return

# int[2]: Alice's score is in the first position, and Bob's score is in the second.
# Input Format

# The first line contains 3 space-separated integers, a[0], a[1], and a[2], the respective values in triplet a.
# The second line contains 3 space-separated integers, b[0], b[1], and b[2], the respective values in triplet b.

# Constraints

# 1 ≤ a[i] ≤ 100
# 1 ≤ b[i] ≤ 100
# Sample Input 0

# 5 6 7
# 3 6 10
# Sample Output 0

# 1 1
# Explanation 0

# Solve:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    ar = [0,0]
    for i in range(len(a)):
        if a[i] > b[i]:
            ar[0] +=1
        if a[i] < b[i]:
            ar[1] +=1
    return ar

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


# Option 2:
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    return [sum(x > y for x, y in zip(a, b)), sum(x < y for x, y in zip(a, b))]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
