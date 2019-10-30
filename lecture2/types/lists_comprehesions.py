S = [x**2 for x in range(9)]
print(S)

M = [x for x in S if x % 2 == 0]
print(M)

allNums = [1, 2, 9, 11, 7, 15, 8, 6]
excludedNums = [2,8,6]

Z = [i for i in allNums if i not in excludedNums]
print('all numbers', allNums)
print('excluded numbers', excludedNums)
print('filtered numbes', Z)


