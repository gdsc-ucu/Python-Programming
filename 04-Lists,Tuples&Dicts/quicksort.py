# Quick sort in Python

# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)

#optimisation of the quick sort
''' This QuickSort requires O(Log n) auxiliary space in
   worst case. '''

#further optimisation

def quickSort(arr, low, high)
  {


while (low < high):
  ''' pi is partitioning index, arr[p] is now
     at right place '''
  pi = partition(arr, low, high);

  # If left part is smaller, then recur for left
  # part and handle right part iteratively
  if (pi - low < high - pi):
    quickSort(arr, low, pi - 1);
    low = pi + 1;

  # Else recur for right part
  else:
    quickSort(arr, pi + 1, high);
    high = pi - 1;

# See below link for complete running code
# https:#ide.geeksforgeeks.org/LHxwPk

# This code is contributed by gauravrajput1
