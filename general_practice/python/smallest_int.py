# given a list represented by variable A, find the smallest positive integer that does not occur in A
# e.g. [1, 3, 6, 4, 1, 2] --> should return 5
# e.g. [-1, -3] --> should return 1

def solution(A):
    # Implement your solution here
    smallest = 1
    A.sort()
    for i in range(len(A)):
        if A[i] == smallest:
            smallest += 1
    return smallest

print(solution([1, 3, 6, 4, 1, 2]))