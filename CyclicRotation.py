def solution(A : list, K):
    if len(A) == 0:
        return A

    for i in range(0,K):
        t = A.pop()
        A.insert(0,t)

    return A