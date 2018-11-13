'''
Title:          Merge sort
Description:    Algorithm for sorting Player objects based on their points in descending order
Author:         Teemu Pätsi
Date:           12th of November 2018
Version:        1.2.1
Python version: 3.6
Usage:          * Keep this file and empty __init__.py in same repository as yatzy.py
		* Must have 'from mergesort import mergesort' line at the beginning of yatzy.py
Notes:		This file is part of yatzy.py file. This game is my a final assignment for Data Structures and Algorithms course in JAMK University of Applied Sciences.

Change log:

2018: 
	12th of November:
		1.1.0   Added exception handler to ensure list only contains integers or floats
		1.1.1   Edited author notes and made some code layout standardizing
	13th of November:
		1.2.0	Done changes for yatzy.py so that my_list is a list of Player objects
		1.2.1	Corrected comments and author notes
		
'''

def mergesort(my_list):
    
    # Exception handler to ensure list only contains integers or floats
	try:
		for element in my_list:
			if (not element.total == float(element.total)):
				raise ValueError
	except ValueError:
		print("\nFunction mergesort only accepts lists consisting of integers or floats\nSorting was unsuccessful!\n")
	else:
		split(my_list)

# Splits my_list to sorted sublists
def split(my_list):
   
    # print("Split " + str(my_list))       # Delete comment to print whenever program splits list to smaller sublists

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

        # Change to ascending sort by changing '>' to '<'
        if left[i].total > right[j].total:
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
 
    # print("Merge " + str(my_list))      # Delete comment to print when program merges two sublists

def main():
    print("Executed main from mergesort.py")

if(__name__ == '__main__'):
    main()
