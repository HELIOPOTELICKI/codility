def solution(N):
    numero = bin(N)[2:]
    c = 0
    maior = 0
    ultimo = 0

    for i in numero:
        if i == '0' and ultimo == '0':
            c += 1
        elif i == '0' and ultimo != '0':
            c = 1
        elif i != '0':
            if c > maior:
                maior = c

        ultimo = i

    return maior