the_dict = {}

the_list = [1,1,1,2,3]

for i in range(len(the_list)):
    if the_list[i] not in the_dict:
        the_dict[the_list[i]] = 1
    else:
        the_dict[the_list[i]] += 1

print(the_dict)


# another way
# from collections import Counter

# new_dict = Counter(the_list)
# print(new_dict)

