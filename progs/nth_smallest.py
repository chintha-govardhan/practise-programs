"""
Program to find the nth smallest element in an unsorted array
with O(nlogn) complexity

"""

def find_nth_smallest(array, n):
    """

    :param array: unsorted list of integers
    :param n: smallest position eg. 2 or 3 smallest
    :return: nth smallest number in the list
    """
    min = []
    max = []

    if len(array) == 0:
        return None

    # segreate number into min and max lists referent to first number in the list
    for i in range(1, len(array)):
        if array[i] < array[0]:
            min.append(array[i])
        elif array[i] > array[0]:
            max.append(array[i])

    """ 
        if the length of min list is one less than n, 
        then the array[0] is the nth smallest number
    """

    if len(min) == n-1:
        return array[0]
    
    """
      if the length of min list is greater than n-1,
      then the nth smallest is likely present in min list
      so repeat find nth smallest with min list
    """
    
    if len(min) > n-1:
        return find_nth_smallest(min, n)
    """
      if the length of min list is less than n-1
      then the nth smallest number likely present in the max list
      so repeat find nth smallest with the max list
    """
    if len(min) < n-1:
        return find_nth_smallest(max, (n-(len(min)+1)))

def test():

    array = [10, 6, 9, 10, 24, 88, 4, 3, 100, 1]
    print(sorted(array))  # display for easy to cross verify

    for i in range(10):
       print(i+1, "-->", find_nth_smallest(array, i+1))

if __name__ == '__main__':
   test()
