def binary_search(array, target):
    lower = -1
    upper = len(array)
    while not (lower + 1 == upper):
        mid = (lower + upper) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            # search lower region
            upper = mid
        else:
            # search upper region
            lower = mid
    
    return -1