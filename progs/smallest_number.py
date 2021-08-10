import sys


def isSorted(datalist, ascending=True):

    if len(datalist) == 1:
        return True

    if ascending:
        for i,j in enumerate(datalist[1:]):
            if j <= datalist[i]:
               return False
    else:
        for i,j in enumerate(datalist[1:]):
            if j >= datalist[i]:
               return False
    return True


def findNextSmallest(nstr):

    nstr1 = [ int(i) for i in nstr ]
    #check if sorted descending, next smallest not possible
    if isSorted(nstr1, False):
        return None

    #check if sorted ascending, swap last two number for next smallest
    if isSorted(nstr1):
        nstr1[-2], nstr1[-1] = nstr1[-1], nstr1[-2]
        return int(''.join([ str(i) for i in nstr1 ]))

    
    # find the first digit < previous digit from right side
    s = []
    size = len(nstr1)

    for i in range(size-1,0,-1):
        if nstr1[i] > nstr1[i-1]:
            smalldigit = max(nstr1[i:])
            for n in nstr1[i:]:
                if n > nstr1[i-1] and n < smalldigit:
                    smalldigit = n
            if smalldigit > nstr1[i-1]:
               j = nstr1[::-1].index(smalldigit)
               nstr1[size-1-j] = nstr1[i-1]
               nstr1[i-1] = smalldigit

            s = nstr1[i:]
            s.sort()
            nstr1 = nstr1[:i] + s
            return int(''.join([ str(k) for k in nstr1 ]))

    return None

nstr = sys.argv[1]

#nstr = "54312"

x = findNextSmallest(nstr)
print(x)


