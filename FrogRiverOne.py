def solution(X, A):
    set1 = set()
    for i, item in enumerate(A):
        set1.add(item)
        if len(set1) == X:
            return i

    return -1


