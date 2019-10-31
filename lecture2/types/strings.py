# -*- coding: UTF-8 -*-  #This is only for python 2

pc = 'półciężarówka'

print(type(pc),pc)

c = pc[3:]
print(c) 
print(pc[0])
print(pc[-1])
print(pc[0:3])
print(len(pc))

print('------------------------------')
PC = pc.replace('ówka','ówa')
print(pc)
print(PC)

print('------------------------------')
msg = """To jest bardzo
długi tekst, który
jest podzielony na
kilka linii"""

print(msg)
print(msg.count('\n'))

# print(dir(msg))
print('------------------------------')
# Side comment, how to nicely concatenate string
names = 'apple','jabłko','apfel'
print('='.join(names))

print('------------------------------')
line = '1, 2, 3, 4'
items = [x.strip() for x in line.split(',')]
print(items)


