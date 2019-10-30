import sys

print(sys.getrefcount(61))
a = 61
print('after assignment to a: ', sys.getrefcount(61))
b = 61
print('after assignment to b: ', sys.getrefcount(61))
