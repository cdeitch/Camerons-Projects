x, y, z = int(input()), int(input()), int(input())


def binaryK(k):
    K = []
    tmp = k
    i = 0
    while tmp > 0:
        K.append(tmp%2)
        tmp = int((tmp-K[i])/2)
        i += 1
    return K


def ModularExpo(a, K, n):
    if n == 1:
        return 0
    b = 1
    if not K:
        return b
    A = a*1
    if K[0] == 1:
        b = a*1
    for i in range(1, len(K)):
        A = int(A*A % n)
        if K[i] == 1:
            b = int(A*b % n)
    return b


w = binaryK(y)
v = ModularExpo(x, w, z)
print(v)
print(pow(x, y, z))
