'''
A left rotation operation on an array shifts each of the array's elements unit to the left. For example, if left rotations are performed on array [1,2,3,4,5], 
then the array would become [3,4,5,1,2].

Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.

Given an array a of n integers and a number, d, perform d left rotations on the array. 

Return the updated array to be printed as a single line of space-separated integers.
'''

'''
a = the array to rotate
d = the number of rotations
'''

def rotLeft(a, d):
    # Write your code here
    result_array = []
    remaining_array = []
    
	# retrieve list items that will be appended to the back of the list i.e. this will cause the remaining list items to move to the left
    for i in range(d):
        result_array.append(a[i])
    
	# retrieve the remaining list items that will not be affected by the rotation using list slicing
    remaining_array = a[d:]
    
	# append the remaining list items to the front of the list in sequential order
    for i in range(len(remaining_array)):
        result_array.insert(i, remaining_array[i])
            
    return result_array


if __name__ == "__main__":
	print(rotLeft([1,2,3,4,5], 2))