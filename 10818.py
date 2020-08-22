import sys
n, *a = map(int, sys.stdin.read().split())
print(min(a), max(a))