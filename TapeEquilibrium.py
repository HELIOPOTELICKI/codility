def solution(A):
    if len(A) == 2:
        if A[0] > A[1]:
            return A[0] - A[1]
        else:
            return A[1] - A[0]

    c = A[0]
    m = sum(A[1:])

    dif = abs(m - c)

    for i in range(1,len(A) - 1):
        c += A[i]
        m -= A[i]
        if abs(c - m) < dif:
            dif = abs(c - m)

    return dif
