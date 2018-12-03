import random
import pdb
from datetime import datetime

comparisons = 0

def merge_sort(array):
    
    split(array)
    print("Array sorted!")
    global comparisons
    print("Program made " + str(comparisons) + " comparisons")
    comparisons = 0


# Splits array to sorted subarrays
def split(array):
    # print ("Split " + str(array))     # Delete comment to print when program splits array block to smaller subarrays
   
    # 1 or 0 length array/substring is sorted
    if len(array) > 1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]
        
        # Recursively splits array until subarray reaches length of 1
        split(left)
        split(right)

        # Merges sorted subarrays
        merge(array, left, right)

# Merges sorted subarrays
def merge(array, left, right):
    i = j = k = 0
    
    # If both sides have still unsorted numbers
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
        global comparisons
        comparisons = comparisons + 1
        
    
    # If other subarray is empty, push rest of other side to the array due it's already sorted 
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1
 
   # print ("Merge " + str(array))      # Delete comment to print when program merges two subarrays


# Checks that program prints elapsed time right (not -320ms but 780ms)
def time_check (start, stop):
    milliseconds = (stop.microsecond - start.microsecond) // 1000
    seconds = stop.second - start.second
    minutes = stop.minute - start.minute
    hours = stop.hour - start.hour

    if milliseconds < 0:
        milliseconds += 1000
        seconds -= 1
    if seconds < 0:
        seconds += 60
        minutes -= 1
    if minutes < 0:
        minutes += 60
        hours -= 1
    if hours < 0:
        hours += 24

    return hours, minutes, seconds, milliseconds

# Tests merge_sort function with <how_many> amount of integers
def test_merge_sort(how_many):
    print ("\nInitializing array with " + str(how_many) + " integers")
    array_init_start = datetime.now()

    array = []
    for x in range (0, how_many):
        array.append(random.randrange(-1000000,1000001))

    array_init_hour, array_init_min, array_init_sec, array_init_ms = time_check(array_init_start, datetime.now())

    # Print how long array init took
    print ("Array's initialization took ", end='')
    time_print(array_init_hour, array_init_min, array_init_sec, array_init_ms)   
    

    sort_start = datetime.now()
    merge_sort(array)
    sort_hour, sort_min, sort_sec, sort_ms = time_check(sort_start, datetime.now())

    # Print how long sorting took
    print ("Sorting took ", end='')
    time_print(sort_hour, sort_min, sort_sec, sort_ms) 

def time_print(hour, mins, sec, ms):
    if (hour > 0):
        print(str(hour) + "hr ", end='')
    if (mins > 0):
        print(str(mins) + "min ", end='')
    if (sec > 0):
        print(str(sec) + "sec ", end='')
    if (hour > 0 or mins > 0 or sec > 0):
        print ("and ", end='')
    
    print(str(ms) + "ms")

   



def main():
    
    test_merge_sort(1000)
    test_merge_sort(10000)
    test_merge_sort(100000)
    test_merge_sort(1000000)
    test_merge_sort(10000000)
    test_merge_sort(100000000)
    test_merge_sort(250000000)

if __name__ == '__main__':
    main()
