'''
Title:          Merge sort
Description:    Algorithm for sorting integers in ascending order
Author:         Teemu Patsi
Date:           12th of November 2018
Version:        1.1.1
Python version: 2.7
Usage:          
    1st way     * Clone this repository
                * Import mergesort to python script
                * mergesort(your_unsorted_list)
                    --> your_unsorted_list becomes sorted in ascending order
   
   2nd way      * Make one or more lists to main()
                * Assign them to mergesort      // mergesort(your_unsorted_list)
                    --> your_unsorted_list becomes sorted in ascending order

Change log:
    1.1.0       Added exception handler to ensure list only contains integers or floats
    1.1.1       Edited author notes and made some code layout standardizing
'''

def mergesort(my_list):
    
    # Exception handler to ensure list only contains integers or floats
    try:
        for element in my_list:
            if(not element == float(element)):
                raise ValueError
    except ValueError:
        print("\nFunction mergesort only accepts lists consisting of integers or floats\nSorting was unsuccessful!\n")
    else:
        split(my_list)

# Splits my_list to sorted sublists
def split(my_list):
   
    print("Split " + str(my_list))       # Delete comment to print whenever program splits list to smaller sublists

    # 1 or 0 length my_list/substring is sorted
    if len(my_list) > 1:
        mid = len(my_list)//2
        left = my_list[:mid]
        right = my_list[mid:]
        
        # Recursively splits my_list until sublist reaches length of 1
        split(left)
        split(right)

        # Merges sorted sublists
        merge(my_list, left, right)

# Merges sorted sublists
def merge(my_list, left, right):
   
    i = j = k = 0
    
    # If both sides have still unsorted numbers
    while i < len(left) and j < len(right):

        # Change to descending sort by changing '<' to '>'
        if left[i] < right[j]:
            my_list[k] = left[i]
            i += 1
        else:
            my_list[k] = right[j]
            j += 1
        k += 1
    
    # If other sublist is empty, push rest of other side to the my_list due it's already sorted 
    while i < len(left):
        my_list[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        my_list[k] = right[j]
        j += 1
        k += 1
 
    print("Merge " + str(my_list))      # Delete comment to print when program merges two sublists

def main():
    print("Executed main from mergesort.py")

if(__name__ == '__main__'):
    main()
