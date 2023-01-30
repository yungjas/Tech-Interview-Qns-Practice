thisset = {"apple", "banana", "cherry"}

# since elements of set cannot be referred to using index or keys, this is the only way to loop thru it
for x in thisset:
    print(x)

# check if banana is present in thisset
print("banana" in thisset)

# add item to a set
thisset.add("orange")
print(f"set after adding orange: {thisset}")

# add items from another set into current set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(f"after adding items from another set into thisset: {thisset}")

# add any iterable into a set
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(f"after adding mylist elements to thisset: {thisset}")

# return new set after combining items from both sets
thisset = {"apple", "banana", "cherry"}
nextset = {1, 2, 3}
finalset = thisset.union(nextset)
print(f"finalset: {finalset}")

# keep only the items present in both sets
thisset = {"apple", "banana", "cherry"}
nextset = {"google", "microsoft", "apple"}
thisset.intersection_update(nextset)
print(f"intersection_update result: {thisset}")

# return new set which contains items in both sets
thisset = {"apple", "banana", "cherry", "google"}
nextset = {"google", "microsoft", "apple"}
finalset = thisset.intersection(nextset)
print(f"intersection result: {finalset}")

# keep only the items that are not present in both sets
thisset = {"apple", "banana", "cherry"}
nextset = {"google", "microsoft", "apple"}
thisset.symmetric_difference_update(nextset)
print(f"symmetric_difference_update result: {thisset}")

# return a new set that contains items not present in both sets
thisset = {"apple", "banana", "cherry"}
nextset = {"google", "microsoft", "apple"}
finalset = thisset.symmetric_difference(nextset)
print(f"symmetric_difference result: {finalset}")

# return a new set that contains items that are only one set and not the other set
thisset = {"apple", "banana", "cherry"}
nextset = {"google", "microsoft", "apple"}
diffset = thisset.difference(nextset)
print(f"difference result: {diffset}")