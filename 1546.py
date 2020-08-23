import sys
n,*a = map(int, sys.stdin.read().split())
print(sum(a)/len(a)/max(a)*100)