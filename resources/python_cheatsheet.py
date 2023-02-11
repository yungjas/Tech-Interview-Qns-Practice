'''
PRINT:
'''
# print each variable in the same line, separate them by space
print(line, end=" ")


'''
READ INPUT:
'''
import sys
for line in sys.stdin:
    print(line.rstrip())


'''
LIST METHODS:
'''
append()	# Adds an element at the end of the list
clear()	    # Removes all the elements from the list
copy()	    # Returns a copy of the list
count()	    # Returns the number of elements with the specified value
extend()	# Add the elements of a list (or any iterable), to the end of the current list
index()	    # Returns the index of the first element with the specified value
insert()	# Adds an element at the specified position e.g. list1.insert(0, test) --> insert at 1st position of the list with the string "test"
pop()	    # Removes the element at the specified position e.g. list1.pop(0) --> deletes 1st element of list1. The default value is -1 which means last item of the list is popped out
remove()	# Removes the first item with the specified value
reverse()	# Reverses the order of the list
sort()      # Sorts the list, add reverse=True if want to sort in desc order
a[1: ]      # Select all elements starting from the 2nd element in the list --> list slicing

# loop through a list
list_test = [1, 2, 3]
list_test2 = [4, 5, 6]
for each_elem in list_test: # with value
    print(each_elem)
for i in range(len(list_test)): # with index
    print(list_test[i])
for i, n in enumerate(list_test): # with index and value
    print(i, n)
for n1, n2 in zip(list_test, list_test2): # loop thru multiple lists simultaneously with unpacking --> output: 1 4 \n(next line) 2 5 \n(next line) 3 6
    print(n1, n2)

# sorting list using custom attributes
list_str = ["Alice", "Bob", "Jasmine"]
list_str.sort(key=lambda x: len(x)) # sort in asc based on length of each string

# turn list into dict
from collections import Counter

the_list = [1,1,1,2,3]
new_dict = Counter(the_list)
print(new_dict)


'''
STRING METHODS:
'''
capitalize()    # Converts the first character to upper case
casefold()	    # Converts string into lower case
center()	    # Returns a centered string
count()	        # Returns the number of times a specified value occurs in a string
encode()	    # Returns an encoded version of the string
endswith()	    # Returns true if the string ends with the specified value
expandtabs()	# Sets the tab size of the string
find()	        # Searches the string for a specified value and returns the position of where it was found
format()	    # Formats specified values in a string
format_map()	# Formats specified values in a string
index()	        # Searches the string for a specified value and returns the position of where it was found
isalnum()	    # Returns True if all characters in the string are alphanumeric
isalpha()	    # Returns True if all characters in the string are alphabets
isascii()	    # Returns True if all characters in the string are ascii characters
isdecimal()	    # Returns True if all characters in the string are decimals
isdigit()	    # Returns True if all characters in the string are digits
isidentifier()	# Returns True if the string is an identifier
islower()	    # Returns True if all characters in the string are lower case
isnumeric()	    # Returns True if all characters in the string are numeric
isprintable()	# Returns True if all characters in the string are printable
isspace()	    # Returns True if all characters in the string are whitespaces
istitle() 	    # Returns True if the string follows the rules of a title
isupper()	    # Returns True if all characters in the string are upper case
join()	        # Converts the elements of an iterable into a string
ljust()	        # Adds padding to the right of the string
lower()	        # Converts a string into lower case
lstrip()	    # Returns a left trim version of the string
maketrans()	    # Returns a translation table to be used in translations
partition()	    # Returns a tuple where the string is parted into three parts
replace()	    # Returns a string where a specified value is replaced with a specified value
rfind()	        # Searches the string for a specified value and returns the last position of where it was found
rindex()	    # Searches the string for a specified value and returns the last position of where it was found
rjust()	        # Adds padding to the left of the string
rpartition()	# Returns a tuple where the string is parted into three parts
rsplit()	    # Splits the string at the specified separator, and returns a list
rstrip()	    # Returns a right trim version of the string
split()	        # Splits the string at the specified separator, and returns a list e.g. "Hi, there, jasmine".split(",") will yield ["Hi", "there", "jasmine"]
splitlines()	# Splits the string at line breaks and returns a list
startswith()	# Returns true if the string starts with the specified value
strip()	        # Returns a trimmed version of the string
swapcase()	    # Swaps cases, lower case becomes upper case and vice versa
title()	        # Converts the first character of each word to upper case
translate()	    # Returns a translated string, first para takes in a character that you want to change, second para takes in a character you want the first character to change to
upper()	      # Converts a string into upper case
zfill()	        # Fills the string with a specified number of 0 values at the beginning

# loop through a string
str1 = "help"
for each_elem in str1:
    print(each_elem)

# to convert string to list, can do the following:
list_str = list(str1)

# string slicing
b = "Hello, World!"
print(b[2:5]) # prints characters from position 2 to 4 --> outputs "llo"

# reverse a string
str2 = "hi"
print(str2[::-1])

# getting ascii value of a character
print(ord("a"))
print(ord("b"))


'''
DICTIONARY METHODS:
'''
clear()	        # Removes all the elements from the dictionary
copy()	        # Returns a copy of the dictionary
fromkeys()	    # Returns a dictionary with the specified keys and value
get()	        # Returns the value of the specified key
items()	        # Returns a list containing a tuple for each key value pair
keys()	        # Returns a list containing the dictionary's keys
pop()	        # Removes the element with the specified key
popitem()	    # Removes the last inserted key-value pair
setdefault()	# Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    # Updates the dictionary with the specified key-value pairs
values()	    # Returns a list of all the values in the dictionary

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# loop through a dictionary and print all key names
for each_key in thisdict:
    print(each_key)

# loop through a dictionary and print all values
for each_key in thisdict:
    print(this_dict[each_key])

# loop through a dictionary and print all keys and its corresponding values
for x, y in thisdict.items():
    print(x, y)


'''
TUPLE METHODS:
'''
count()	# Returns the number of times a specified value occurs in a tuple
index()	# Searches the tuple for a specified value and returns the position of where it was found

# loop through a tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# can be used as keys for dict
my_dict = {(1, 2): 3}

# can be used as keys for set
my_set = set()
my_set.add((1, 2))
print((1, 2) in my_set) # result: true


'''
HEAPS (a concrete implementation of the priority queue using an array):
It can be conceptually represented as a particular binary tree
'''
import heapq

# Min Heap: smallest to largest
minHeap = [] # under the hood they are arrays
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4) # minHeap looks like this currently: [2, 3, 4]
print(minHeap[0]) # min value is always at index 0

# Max Heap: largest to smallest
# since python doesn't support max heap and only min heap, we can use negative numbers to store from largest to smallest:
maxHeap = []
heapq.heappush(minHeap, -3)
heapq.heappush(minHeap, -2)
heapq.heappush(minHeap, -4) # maxHeap looks like this currently: [-4, -3, -2]

# max value is always at index 0, but have to multiply by -1 to negate the negative value aka make it positive
print(-1 * maxHeap[0])

# build heap from initial values
# useful when you want to sort list but want it to be slightly faster (sort is O(n log n) which is slower than using heap which is linear time O(n))
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
# loop thru the heap and keep printing the values --> result: 
# 1
# 2
# 4
# 5
# 8
while arr:
    print(heapq.heappop(arr))


'''
INHERITENCE:
'''
class Staff:
    def __init__(self, name="", department="",
                 date_of_joining=datetime.today(),
                 base_salary=0):
        self.name = name
        self.department = department
        self.date_of_joining = date_of_joining
        self.base_salary = base_salary

    def get_salary(self):
        return self.base_salary

# Manager has its own attributes i.e. bonus perk
class Manager(Staff):
    def __init__(self, name="", department="",
                 date_of_joining=datetime.today(),
                 base_salary=0,
                 bonus_perk=0):
        # inherit from Staff class
        Staff.__init__(self, name, department, date_of_joining,
                       base_salary)
        # this attribute is only specific to managers
        self.bonus_perk = bonus_perk

    # polymorphic method
    def get_salary(self):
        return self.base_salary + self.bonus_perk


'''
STACK:
'''
# Stack: Last In First Out
class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, data):
        return self.items.append(data)
    
    def pop(self):
        # removes the last item that has entered the stack
        return self.items.pop()  


'''
QUEUE:
'''
# Queue: First In First Out
class Queuee:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def enqueue(self, data):
        self.items.append(data)
    
    def dequeue(self):
        # remove the 1st item of the queue
        return self.items.pop(0)


'''
DOUBLE-ENDED QUEUE (elements can be added or removed from either the front or back):
'''
from collections import deque

queue = deque()
queue.append(1) # add 1 to the back of the queue (right side)
queue.append(2) # add 2 to the back of the queue (right side)
print(queue) # result: dequeue([1, 2])

queue.popleft() # remove element on the leftmost side of the queue
print(queue) # result: dequeue([2])

queue.appendleft(1) # add value to the leftmost of the queue
print(queue) # result: dequeue([1, 2])

queue.pop() # pop from the right side
print(queue) # result: dequeue([1])


'''
DFS:
'''
# Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5')


'''
BFS:
'''
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] # List for visited nodes.
queue = []     # Initialize a queue

def bfs(visited, graph, node): # function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')    # function calling


'''
BINARY SEARCH:
'''
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