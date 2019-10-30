name = 'Euzebiusz'   
a, b =  1,2        # przypisanie rozpakowujące krotkę
c, d = [1,2]       # przypisanie rozpakowujące listę

a,b,c,d = [1,2,3,4]

first, *other = [1, 2, 3, 4] # rozszerzone przypisanie sekwencji (Python 3)
print(first, other)

first,*other,last = [1,2,3,4]
print(first, other, last)


a += 42  # przypisanie rozszerzone
