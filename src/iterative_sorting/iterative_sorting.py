# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index +1, len(arr)):#Loop thru items in the unsorted part of the list
            if arr[j] < arr[smallest_index]:#Check if the current item in the loop is less than the current smallest item
                smallest_index = j#If so change smallest item
        # TO-DO: swap
        if smallest_index != i:
            arr[smallest_index], arr[i] = arr[i], arr[smallest_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(0, len(arr) -1):
            index_one = arr[i]
            index_two = arr[i+1]
            if index_two < index_one:
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
                swapped = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr


test = [8,5,3,4,9,2]
print(bubble_sort(test))