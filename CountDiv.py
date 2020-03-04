def solution(A, B, K):
    c = 0
    if A % K == 0:
        for i in range(A, B + 1, K):
            c += 1
    else:
        m = A - K
        A += m
        for i in range(A, B + 1, K):
            c += 1

    return c
