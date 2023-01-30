def negative_list():
    # -1 refers to the last item, in this case its mango
    # kiwi will be -2, orange will be -3 etc
    test_list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
    # -4 inclusive and -1 exclusive
    # will return cherry, orange, kiwi
    return test_list[-4:-1]

print(f"negative_list result: {negative_list()}")

def check_list():
    test_list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
    if "apple" in test_list:
        return True
    return False

print("check_list result: " + str(check_list()))


def change_list1():
    test_list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
    # replace the 2nd and third element
    # list indexing --> 1 is inclusive and 3 is exclusive
    test_list[1:3] = ["blackcurrent", "watermelon"]
    return test_list

print(f"change_list1 result: {change_list1()}")

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
def change_list2():
    test_list = ["apple", "banana", "cherry"]
    # banana at index 1 will be replaced with blackcurrant
    # watermelon will be inserted in index 2
    test_list[1:3] = ["blackcurrant", "watermelon"]
    return test_list

print(f"change_list2 result: {change_list2()}")

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
def change_list3():
    test_list = ["apple", "banana", "cherry"]
    # watermelon will be inserted in index 1, banana and cherry will be removed from the list
    test_list[1:3] = ["watermelon"]
    return test_list

print(f"change_list3 result: {change_list3()}")

# list comprehension
def list_compre():
    test_list = ["apple", "banana", "cherry", "kiwi", "mango"]
    new_list = [x for x in test_list if "a" in x]
    return new_list

print(f"list_compre result: {list_compre()}")

def list_compre2():
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_list = [x for x in test_list if x % 2 == 0]
    return new_list

print(f"list_compre2 result: {list_compre2()}")

def list_compre3():
    test_list = ["apple", "banana", "cherry", "kiwi", "mango"]
    # return element if it is not banana, if it is banana return orange
    new_list = [x if x != "banana" else "orange" for x in test_list]
    return new_list

print(f"list_compre3 result: {list_compre3()}")

# sort the list based on how close the number is to 50
def myfunc(n):
    return abs(n - 50)

num_list = [100, 50, 65, 82, 23]
num_list.sort(key = myfunc)
print(f"num_list results after myfunc{num_list}")