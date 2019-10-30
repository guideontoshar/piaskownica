import itertools
def appender(L, val, ntimes):
    """This function appends val ntimes to the list L.
    """
    L.extend(itertools.repeat(val, ntimes))


if __name__ == '__main__':
    mylist = [1,2,3]
    appender(mylist, 22, 3)
    print(mylist)
