while True:
    x = input('Give positive integer : ')
    if int(x) > 0:
        print("You gave: %s" % x)
    else:
        break


from random import random

i = 1
while i < 10:
    r = random()
    if r >= 0.9:
        break
    print("%3.2f"%r)
    i+=1
