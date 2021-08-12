"""
  1 2 3
  4 5 6
  7 8 9

  1 2 3
  6 9 8
  7 4 5
"""
from itertools import islice


i = [ [1,2,3], [4,5,6], [7,8,9] ]
k = [ [1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25] ]

def print_matrix(m):

    for row in m:
        print("")
        for col in row:
            print(col,end='\t')
    print("\n")

def slices(m, sl):

    tl = int(len(m)/sl)
    ai = iter(m)
    return [ list(islice(ai, sl)) for i in range(tl) ]


def chain_print(m):

    x, y = len(m), len(m[0])

    if x == 1 and y == 1:
        return m[0]

    d = []
    # print first row
    for i in m[0]:
        d.append(i)

    # print last col
    for i in m[1:]:
        d.append(i[-1])

    # print last row in reverse direction
    for i in m[-1][:-1][::-1]:
        d.append(i)

    # print first col in reverse except (0,0) entry
    for i in m[1:][:-1][::-1]:
        d.append(i[0])

    # extract inner matrix
    m1 = [ im[1:-1] for im in m[1:-1] ]
    d1 = chain_print(m1)
    d.extend(d1)

#    print_matrix(slices(d, y))

    return d

print_matrix(k)
d = chain_print(k)
print_matrix(slices(d, len(k[0])))
