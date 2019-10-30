i = 1234
print(type(i),i)

big = 2**200
print(type(big),big)

f = 4.1e210
print(type(f), f)

octal = 0o17
print(type(octal), octal)

hex = 0xaa
print(type(hex), hex)

bin = 0b101
print(type(bin), bin)

z = 3+4j
print(type(z), z)

flag = True
print(type(flag), flag)

# floating point with fixed precision 
import decimal
from decimal import Decimal

d = 0.1 + 0.1 + 0.1 - 0.3
print(type(d), d)

d = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
print(type(d), d)

decimal.getcontext().prec = 4
print("floating division ", 1/7)
print("decimal division ", Decimal(1) / Decimal(7))

# Fractions
from fractions import Fraction
x = Fraction(1,3)
y = Fraction(4,6)
print(type(y), y)
print(Fraction('1.25'))
print(Fraction(2/6))
