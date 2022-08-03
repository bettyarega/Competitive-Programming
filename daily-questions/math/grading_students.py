import math
import os
import random
import re
import sys


def next_multiple_of_five(grade):
    if(grade % 10 < 5):
        return (grade // 10) * 10 + 5
    elif( grade % 10 > 5):
        return (grade // 10) *10 +10
    elif(grade % 10 == 0 | grade % 10 == 5):
        return grade        
    
def gradingStudents(grades):
    grades_final = []
    for grades_item in grades:
        nxt_multiple_of_five = int(next_multiple_of_five(grades_item))
        if(grades_item < 38):
            grades_final.append(grades_item)
        elif(nxt_multiple_of_five - grades_item < 3):
            grades_final.append(nxt_multiple_of_five)
        elif(nxt_multiple_of_five - grades_item >= 3):
            grades_final.append(grades_item)
    return grades_final

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