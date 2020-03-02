def solution(X, Y, D):
    if X == Y:
        return 0

    Y -= X

    if Y % D != 0:
        return (Y // D) + 1

    return Y//D

