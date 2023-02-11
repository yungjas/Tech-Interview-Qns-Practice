# We will create our own dynamic array class by using the built-in library class in python called ctypes which is going to be used as a raw array from the ctypes module.
# followed this tutorial: https://www.educative.io/answers/how-to-implement-dynamic-array-in-python
import ctypes

class DynamicArray:
    def __init__(self):
        self.n = 0 # count elements
        self.size = 1 # default array capacity
        self.A = self.make_array(self.size) # make a static array with the default capacity
    
    def __len__(self):
        return self.n
    
    def append(self, item):
        # if we are trying to append a new element but the current static array does not have enough space
        if self.n == self.size:
            # double the capacity of the new static array
            self.resize(2*self.size)
        # insert the item into the new static array
        self.A[self.n] = item
        # increase the count of the number of elements by 1 since we are adding 1 item
        self.n += 1
    
    def resize(self, new_capacity):
        # create a new static array
        B = self.make_array(new_capacity)
        
        # updates self.size with the new capacity
        self.size = new_capacity

        # copy elements from the old static array into the new static array
        for i in range(self.n):
            B[i] = self.A[i]
        
        # replace the current static array with the new static array
        self.A = B
    
    def make_array(self, new_capacity):
        # makes the new static array with the new capacity
        return (new_capacity * ctypes.py_object)()
    
    def __str__(self):
        temp = ""
        for i in range(self.n):
            temp = temp + str(self.A[i]) + ","
        # removes the extra , at the end
        temp = temp[:-1]
        return "[" + temp + "]"


dynamic_arr = DynamicArray()
dynamic_arr.append(100)
dynamic_arr.append(200)
dynamic_arr.append(500)
print(len(dynamic_arr))
print(dynamic_arr)