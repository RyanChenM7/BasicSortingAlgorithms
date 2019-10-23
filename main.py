# A mini-project which plots out operations vs arrayLength for BubbleSort, InsertionSort, and SelectionSort.
import matplotlib.pyplot as plt
import math
import random

# A reversed sorted list for testing the functionality of the sorting algorithms
worst_case = list(range(1,11))[::-1]


count = 0
# Make a function that adds one to count
# Will show up everytime an elementary operation occurs
def c():
    global count
    count += 1

# Optimised bubble sort from last assignment
def bs_optimized(arr):

    for i in range(len(arr)-1):
        # The aforementioned boolean to keep track of swaps
        flag = False; c()

        # Don't check the last i because they are guaranteed to be sorted already
        for j in range(len(arr)-1-i):
            c()
            if arr[j] > arr[j+1]:
                flag = True; c()
                arr[j+1], arr[j] = arr[j], arr[j+1]; c()
        
        c()
        if flag == False:
            break; c()

    c()
    # Return sorted array
    return arr


# Selection Sort Implementation
def select_sort(arr):
    # The sorted segment will be constructed from the left side

    for i in range(len(arr)-1):
    # Arbitrarily initialize min element index
        min_index = i; c()

        # i will change the left-bound of the unsorted array
        for j in range(i+1, len(arr)):

            # The standard way to find the minimum element in an array
            c()
            if arr[j] < arr[min_index]:
                min_index = j; c()

        # Move the min element to end of sorted segment
        arr[i], arr[min_index] = arr[min_index], arr[i]; c()

    c();
    # Return sorted array
    return arr


# Insertion Sort Implementation
def insert_sort(arr):
    # We will be building our sorted segment from left to right
    for i in range(1, len(arr)):
        
        temp = arr[i]; c()

        # Begin our search for the spot to insert arr[i] 
        j = i - 1; c()

        # Stop when j hits 0, the left-bound of the array
        while j >= 0:
            # Swap it backwards until it's in the right spot 
            c()
            if temp >= arr[j]:
                break

            arr[j+1] = arr[j]; c()
            j -= 1; c()

        arr[j+1] = temp; (c)

    # This usage of temp saves elementary moves; better than swapping repeatedly

    c()
    # Return sorted array
    return arr


# N is the max size of unsorted array
N = 300

# Now we grab our data and plot it three times
sorting_functions = [bs_optimized, select_sort, insert_sort]
titles = ["Bubble Sort", "Selection Sort", "Insertion Sort"]
x_label = "Size of Unsorted Array"
y_label = "Number of Operations"
x_values = list(range(1, N+1))

# We have coded in our titles, labels, and x_values.

for index, f in enumerate(sorting_functions):

    arr_sizes = list(range(1,N+1))
    operations = []

    for t in range(1,N+1):

        # Reset elementary operations count
        count = 0 

        # Make a shuffled list of numbers
        test = list(range(1,t+1))
        random.shuffle(test)

        f(test)

        operations.append(count)

    # Plot our data
    fig = plt.figure()

    plt.title(titles[index])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(x_values, operations, label=titles[index], marker=".", color="blue")
    plt.plot(x_values, [n**2 for n in x_values], label='O(n^2)', marker=".", color="red")
    plt.legend(bbox_to_anchor=(1, 1))
    #plt.grid(True)
    plt.tight_layout()
    plt.savefig(titles[index] + '.png')
