def solution(A):
    # Implement your solution here
    trees_cut = 0
    trees_info = [0] * len(A)

    for i in range(len(A)):
        if i < len(A) - 1:
            if A[i] > A[i+1]:
                trees_info[i] = 1
            elif A[i] < A[i+1]:
                trees_info[i] = 0
            else:
                trees_info[i] = -1
        elif (i == len(A) - 1) and A[i] > A[i - 1]:
            trees_info[i] = 1
        elif (i == len(A) - 1) and A[i] < A[i - 1]:
            trees_info[i] = 0 
            # adj = i + 1
            # first = A[0]
            # if (A[i] > A[adj]) or (A[i] < A[adj]):
            #     check += 1
            # elif first > A[i] > :

    return trees_info

print(solution([3, 7, 4, 5]))