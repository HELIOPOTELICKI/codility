def solution(A, B, K):
    c = 0
    for i in range(A,B + 1):
        if i % K == 0:
            c += 1
    return c

print(solution(6,11,2))