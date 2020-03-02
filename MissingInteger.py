def solution(A):
    A.sort()

    if not 1 in A:
        return 1

    for i in range(0,len(A) - 1):
        if A[i] == A[i + 1]:
            continue

        if A[i] != A[i + 1] - 1:
            if A[i] + 1 > 0:
                return A[i] + 1

    return A[len(A) - 1] + 1