n = int(input())
for i in range(n):
    sum = 0
    a = input().split("X")
    for j in a:
        sum = sum + int(len(j)*(len(j)+1)/2)
    print(sum)
