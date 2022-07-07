if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_name_marks = student_marks[query_name]
    query_name_average_mark = sum(query_name_marks)/3
    print("{:.2f}".format(query_name_average_mark))