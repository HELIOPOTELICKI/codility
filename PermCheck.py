def solution(A):

    l = set(A)

    if len(A) != max(A):
        return 0

    if len(l) == max(A):
        return 1

    return 0

l = [4,1,3,2]
print(solution(l))