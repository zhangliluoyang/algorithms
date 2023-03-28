"""
My study notes/solutions for the Coursera course Crafting Quality Code.
3 basic sorting approaches: bubble, selection and insertion
"""

# Bubble Sort
# inner loop: move the largest number to the rightmost position;
# outer loop: keep narrowing down the range of unsorted part;
def bubble_sort(L):
    """(list) -> NoneType
    Sort the items of L from smallest to largest.
    >>> bubble_sort([3, 9, 1, 5, 7])
    [1, 3, 5, 7, 9]
    """
    end = len(L) - 1
    while end != 0:
        for i in range(end):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
        end -= 1

    return L


# Selection Sort
# inner loop: from L[i+1:], select the number smaller than L[i] and swap their positions
# outer loop: increment i to narrow down unsorted part
def select_sort(L):
    """(list)->NoneType
    >>> L = [9, 3, 7, 2, 5]
    >>> select_sort(L)
    [2, 3, 5, 7, 9]
    >>> L = [10, 1, 7, 8, 6]
    >>> select_sort(L)
    [1, 6, 7, 8, 10]
    """
    i = 0
    while i < len(L):
        for j in range(i+1, len(L)):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]
        i += 1

    return L


# Insertion sort
# inner loop: compares L[j] with everything to its left and
#             puts it behind the number smaller than it
# outer loop: keeps moving the start point of the unsorted part to the right
def insertion_sort1(L):
    """(list)->NoneType
    sort the list in ascending order
    >>> insertion_sort1([2, 5, 3, 1])
    [1, 2, 3, 5]
    """
    for i in range(len(L)):
        insert_num = L[i]
        j = i
        while j != 0 and L[j] < L[j-1]:
            L[j] = L[j-1]
            L[j-1] = insert_num
            j -= 1
    return L

# the inner loop is actually a bubble operation;
# so the value-holder variable "insert_num" can be removed,
# and the value re-assigning steps can be replaced with an explicit swap.
def insertion_sort2(L):
    """(list)->NoneType
    sort the list in ascending order
    >>> insertion_sort2([2, 5, 3, 1])
    [1, 2, 3, 5]
    """
    for i in range(len(L)):
        j = i                            # 'while' loop still needed to enable
        while j != 0 and L[j] < L[j-1]:  # bubble sorting in opposite direction
            L[j-1], L[j] = L[j], L[j-1]
            j -= 1

    return L


if __name__ == "__main__":
    import doctest
    doctest.testmod()
