# strings are immutable
s = 'abc'
print(id(s), s)
s += 'def'
print(id(s), s)

# Lists are mutable
L = [1,2,3]
print(id(L), L)
L += [4,5,6]
print(id(L), L)

L[0] = 123
print(L)

s[0] = 'A'
