def flip(target):
    count = 0
    for i in range(len(target)):
        if i == len(target) - 1:
            break
        elif target[i] != "0" and target[i] == target[i+1]:
            count+=1
    return count

print(flip("01011"))
