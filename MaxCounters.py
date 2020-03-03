def solution(N, A):
    l = [0]*N
    m = 0
    m2 = 0
    for i in A:
        if i <= N:
            if m > l[i - 1]:
                l[i - 1] = m
            l[i - 1] += 1
            if m2 < l[i - 1]:
                m2 = l[i - 1]
        else:
            m = m2

    for i in range(0, N):
        if l[i] < m:
            l[i] = m
    return l

l = [3,4,4,6,1,4,4]
print(solution(5, l))

