import sys
L = [1,2,3]
print("Number of refs to value of L: %d" % sys.getrefcount(L))
M = L
print("Number of refs to value of L: %d" % sys.getrefcount(L))

print(L, M)
L[0] = 99
print(L, M)

import copy
M = copy.copy(L)
N = L.copy()
P = L[:]
print("Number of refs to value of L: %d" % sys.getrefcount(L))

L[1] = 22
print(L, M, N, P)
