def solution(N, A):
    l = [0]*N

    m = 0
    for i in A:
        if i < N + 1:
            l[i - 1] += 1
            if l[i - 1] > m:
                m = l[i - 1]
        else:
            l = [m] * N
    return l

l = [3,4,4,6,1,4,4]
print(solution(5, l))
