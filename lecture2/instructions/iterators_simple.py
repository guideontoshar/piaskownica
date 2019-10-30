L = [1,2,3]
for x in L:
    print(x, end=' ')
print()

I = iter(L)
while True:
    try:
        x = next(I)
    except StopIteration:
        break
    print(x, end=' ')
print()

print('----------------------------')
L = ['ala', 'ola', 'ela']
W = ['pies', 'kot', 'chomik']

import itertools

for p in zip(L,W):
    print(p)

print('----------------------------')
for p in zip(L, itertools.count(0,4)):
    print(p)

print('----------------------------')
LL = list(map(lambda s: s.upper(), L)) 
print(LL)
