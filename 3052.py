import sys
def res(a):
    return int(a)%42
a = list(set(list(map(res, sys.stdin.read().split()))))
print(len(a))