A = int(input())
B = int(input())
C = int(input())
n = A*B*C
a = [0]*10
while n != 0:
    a[n%10] = a[n%10] + 1
    n = n//10
for x in a:
    print(x)