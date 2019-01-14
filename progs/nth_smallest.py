"""
Program to find the nth smallest element in an unsorted array
with O(nlogn) complexity

"""

def find_nth_smallest(input, n):

    min = []
    max = []

    if len(input) == 0:
        return None

    for i in range(1, len(input)):
        if input[i] < input[0]:
            min.append(input[i])
        elif input[i] > input[0]:
            max.append(input[i])
    if len(min) == n-1:
        return input[0]
    elif len(min) > n-1:
        return find_nth_smallest(min, n)
    elif len(min) < n-1:
        return find_nth_smallest(max, (n-(len(min)+1)))

def test():

    input = [10, 6, 9, 10, 24, 88, 4, 3, 100, 1]
    print sorted(input)  # display for easy to cross verify

    for i in range(10):
       print i+1, "-->", find_nth_smallest(input, i+1)

if __name__ == '__main__':
   test()
