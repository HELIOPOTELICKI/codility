def solution(X, A):
    set1 = set()
    for i, item in enumerate(A):
        set1.add(item)
        if len(set1) == X:
            return i

    return -1

l = [1,3,1,4,4,3,5,2]

print(solution(5,l))

