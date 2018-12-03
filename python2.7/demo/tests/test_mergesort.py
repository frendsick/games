'''
Title:          Merge sort
Description:    Algorithm for sorting integers in ascending order
Author:         Teemu Pätsi
Date:           12th of November 2018
Version:        1.0.0
Python version: 3.6
Usage:          Run this program to see how my mergesort code works

Change log:
'''

from mergesort import mergesort
import random

# Run through mergesort algorithm and check whether or not sorting was done successfully
def test_mergesort(my_list):
    
    test_mergesort.counter += 1
    mergesort(my_list)
    try:
        for element in my_list:
            if(not element == float(element)):
                raise ValueError
    except ValueError:
        pass
    except:
        print("CONGRATULATIONS you have found bu.. feature from my unbreakable code!\nPlease inform the author how did you do this! :)")
    else:
        if(sorted(my_list) == my_list):
            print("Sorting complete!")
    finally:
        print("Test number " + str(test_mergesort.counter) + " over\n")

# Counts how many tests have been done during this run
test_mergesort.counter = 0

# Test with integers only
how_many = 20
print("Sorting list with " + str(how_many) + " integers")
int_list = []
for x in range (0, 20):
    int_list.append(random.randrange(-1000000,1000001))
test_mergesort(int_list)

# Test with floats and integers
print("Sorting list with integer and float values")
float_list = [1.0, 3.6, -124.72, 20405062, 21042.5, 12456727.2, -200]
test_mergesort(float_list)

# Test with other datatypes (Raises ValueException)
print("Trying to sort list with many different datatypes")
mixed_list = [1, 2.0, 's', "asd"]
test_mergesort(mixed_list)

# Test with already sorted list
sorted_list = [1,2,4,7]
test_mergesort(sorted_list)

# Test with only one element in list
single_list = [1]
test_mergesort(single_list)
