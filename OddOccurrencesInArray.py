def solution(A):
    if len(A) == 1:
        return A[0]
    A.sort()
    for i in range(0,len(A),2):
        if i == len(A) - 1:
            return A[i]
        if A[i + 1] != A[i]:
            return A[i]