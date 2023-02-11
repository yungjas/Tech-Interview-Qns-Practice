# loop through a list
list_test = [1, 2, 3]
list_test2 = [4, 5, 6]
for each_elem in list_test: # with value
    print(each_elem)
for i in range(len(list_test)): # with index
    print(list_test[i])
for i, n in enumerate(list_test): # with index and value
    print(i, n)
for n1, n2 in zip(list_test, list_test2): 
    print(n1, n2)

list_str = ["Alice", "Bob", "Jasmine"]
list_str.sort(key=lambda x: len(x)) # sort in asc based on length of each string
print(list_str)

# create a 4 by 4 list 4 times --> [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
arr = [[0] * 4 for i in range(4)]
print(arr)

arr2 = [[0] * 4] *4
print(arr2)
arr2[1][0] = 1
print(arr2)

my_set = set()
my_set.add((1, 2))
print((1, 2) in my_set)