def solution(A):
        if len(A) == 0:
            return 1

        if len(A) == 1:
            if A[0] == 1:
                return 2
            else:
                return 1

        A.sort()

        if A[0] != 1:
            return 1

        if A[len(A) - 1] != len(A) + 1:
            return len(A) + 1

        for i in range(0,len(A) + 1):
            if A[i] != A[i + 1] - 1:
                return A[i] + 1

        return A[1] + 1


