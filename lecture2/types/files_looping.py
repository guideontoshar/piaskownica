ifile = open('xdata.dat', 'r')
x = []
y = []

for line in ifile.readlines():
    xc =  float(line)
    x.append(xc)
    y.append(xc**2) 
    
ofile = open('xydata.data', 'w')
for xy in zip(x,y):
    ofile.write('x=%f y=%f\n'%xy) 

