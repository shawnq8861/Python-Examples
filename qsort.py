# an implementation of the quick sort algorithm

def qsort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        print "pivot " + str(pivot)
        less = [i for i in array[1:] if i <= pivot]
        print "less " + str(less)
        greater = [i for i in array[1:] if i > pivot]
        print "greater " +str(greater)
        return qsort(less) + [pivot] + qsort(greater)

def main():
    nums = [13, 81, 92, 65, 43, 31, 57, 26, 75, 0]
#    nums = [2, 3, 1, 5, 4]
    print "unsorted array:"
    for num in nums:
        print num
    sorted = qsort(nums)
    print "sorted array:"
    for num in sorted:
        print num    

main()
