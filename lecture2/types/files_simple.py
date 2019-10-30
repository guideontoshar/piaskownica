ifile = open('xdata.dat', 'r')
print(type(ifile))
line = ifile.readline()

x = float(line)

ofile = open('xdata_comment.txt', 'w')
ofile.write("First coord in xdata.dat is : %f\n" % x)

