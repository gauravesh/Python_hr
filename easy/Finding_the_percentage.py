if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    #print(student_marks)
    x=student_marks.get(query_name)
   # print(x)
    s=sum(x)
    print("%.2f" % (s/3))
