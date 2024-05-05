# HackerLand University has the following grading policy:

# Every student receives a grades in the inclusive range from 0 to 100.
# Any grades less than 40 is a failing grade.
# Sam is a professor at the university and likes to round each student's grades according to these rules:

# If the difference between the grades and the next multiple of 5 is less than 3, round grades up to the next multiple of .
# If the value of  is less than , no rounding occurs as the result will still be a failing grade.
# Examples

# grades = 84 round to  (85 - 84 is less than 3)
# grades  = 29 do not round (result is less than 40)
#  grades = 57 do not round (60 - 57 is 3 or higher)
# Given the initial value of  for each of Sam's  students, write code to automate the rounding process.

# Function Description

# Complete the function gradingStudents in the editor below.

# gradingStudents has the following parameter(s):

# int grades[n]: the grades before rounding
# Returns

# int[n]: the grades after rounding as appropriate
# Input Format

# The first line contains a single integer, , the number of students.
# Each line  of the  subsequent lines contains a single integer, .

# Constraints

# Sample Input 0

# 4
# 73
# 67
# 38
# 33
# Sample Output 0

# 75
# 67
# 40
# 33
# Explanation 0

# image

# Student  received a , and the next multiple of  from  is . Since , the student's grade is rounded to .
# Student  received a , and the next multiple of  from  is . Since , the grade will not be modified and the student's final grade is .
# Student  received a , and the next multiple of  from  is . Since , the student's grade will be rounded to .
# Student  received a grade below , so the grade will not be modified and the student's final grade is .

# Solve:
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    grades_list = []
    for i in grades:
        if i <= 40:
            if 40 - i < 3:
                grades_list.append(40)
            else:
                grades_list.append(i)
        else:
            number = i // 5
            if (number+1)*5 - i < 3:
                grades_list.append((number+1)*5)
            else:
                grades_list.append(i)
    return grades_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
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
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    grades_list = []
    for i in grades:
        if i >=38 and i % 5>=3:
            i = i+(5-(i%5))
        grades_list.append(i)
    return grades_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


