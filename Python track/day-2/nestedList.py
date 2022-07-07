import sys

if __name__ == '__main__':
    gradesList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        gradesList.append([name,score])
    lowGrade = sys.maxsize
    secondLowGrade = sys.maxsize
    names = []
    for i in range(len(gradesList)):
        if(gradesList[i][1] < lowGrade):
            lowGrade = gradesList[i][1]
    for i in range(len(gradesList)):
        if(gradesList[i][1] > lowGrade and gradesList[i][1] < secondLowGrade):
            secondLowGrade = gradesList[i][1]
    for i in range(len(gradesList)):
        if(gradesList[i][1] == secondLowGrade):
            names.append(gradesList[i][0])
    names.sort()
    for i in range(len(names)):
        print(names[i])
        
        