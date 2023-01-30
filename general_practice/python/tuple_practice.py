# -1 represents the last item of the tuple, in this case it's mango
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# -4 inclusive and -1 exclusive --> will print out orange, kiwi, melon
print(thistuple[-4:-1])

if "apple" in thistuple:
    print("yes")
else:
    print("no")

# workaround to change tuple elements
tuplelist = list(thistuple) # convert tuple to a list first
tuplelist[1] = "pear" # change the element you want
thistuple = tuple(tuplelist) # convert back to tuple
print(f"tuple after changing {thistuple}") # tadah

# workaround to add elements to tuple
tuplelist = list(thistuple) # convert tuple to a list first
tuplelist.append("grape") # add the element you want
thistuple = tuple(tuplelist) # convert back to tuple
print(f"tuple after adding element {thistuple}") # tadah