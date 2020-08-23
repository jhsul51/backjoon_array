import sys
c = int(input())
for i in range(c):
    n,*a = map(int,sys.stdin.readline().split())
    b = list(a)
    mean = sum(b)/n
    count = 0
    for student in b:
        if(student > mean):
            count += 1
    print("%.3f%%" %(count/n*100))