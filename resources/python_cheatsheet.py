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
pop()	    # Removes the element at the specified position e.g. list1.pop(0) --> deletes 1st element of list1
remove()	# Removes the first item with the specified value
reverse()	# Reverses the order of the list
sort()      # Sorts the list
a[1: ]      # Select all elements starting from the 2nd element in the list --> list slicing

# loop through a list
list = [1, 2, 3]
for each_elem in list:
    print(list)


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
isalpha()	    # Returns True if all characters in the string are in the alphabet
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
ljust()	        # Returns a left justified version of the string
lower()	        # Converts a string into lower case
lstrip()	    # Returns a left trim version of the string
maketrans()	    # Returns a translation table to be used in translations
partition()	    # Returns a tuple where the string is parted into three parts
replace()	    # Returns a string where a specified value is replaced with a specified value
rfind()	        # Searches the string for a specified value and returns the last position of where it was found
rindex()	    # Searches the string for a specified value and returns the last position of where it was found
rjust()	        # Returns a right justified version of the string
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
upper()	        # Converts a string into upper case
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