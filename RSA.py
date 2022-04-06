# Riley Barnes
# cs427
# Python3

import random

descKey = 65537

testp = "9da5"
testq = "b28b"
testn = "6df25297"
testt = "6df10268"
testmssg = "hello, friend"
messagehashtest = "1bcbce1"
privatekeytest = "4a5a9c39"
singedhashtest = "18e1eac9"
uninvertedmsgtest = "1bcbce1"


def prime(n, k):
    if (n <= 3):
        return 1
    r = 0
    d = n - 1
    while ((d // 2) % 2) == 0:
        r += 1
        d = t // 2
    while (k > 0):
        a = random.randrange(range(2, n - 2))
        x = a ** d % n
        if (x == 1 or x == n - 1):
            k-=1
            continue
        j = 0
        while (r-1)>0:
            x = x**2 %n
            if x == n-1:
                j = 1
                break
            r-=1
        if(j == 1):
            continue
        return 0
    return 1
def pows(N, m, d):
    if (d < 0):
        m = 1 // m
        d = -d
    if (d == 0):
        return 1
    y = 1
    while d > 1:
        if (d % 2 == 0):
            m = m * m % N
            d = d // 2
        else:
            y = m * y % N
            m = m * m % N
            d = (d - 1) // 2
    return m * y % N
def elfhash(s):
    h = 0
    high = 0
    for i in s:
        h = (h << 4) + ord(i)
        high = h & int("F0000000", 16)
        if (high):
            h ^= high >> 24
        # need to flip bits
        tempstr = f'{high:032b}'
        tempstr = tempstr.replace('1', '2')
        tempstr = tempstr.replace('0', '1')
        tempstr = tempstr.replace('2', '0')
        high = int(tempstr, 2)
        h &= high
    return h
def uclid(a, n):
    t = 0
    r = n
    newt = 1
    newr = a
    while newr != 0:
        quotient = r // newr
        t, newt = (newt, t - quotient * newt)
        r, newr = (newr, r - quotient * newr)
    if (r > 1):
        return -1
    if (t < 0):
        t = t + n
    return t


def rsasign(message):
    messagehash = elfhash(message)
    print(hex(messagehash))
    # todo prime function for p and q
    p = int(testp, 16)
    q = int(testq, 16)
    N = q * p
    print(hex(N))
    totient = (q - 1) * (p - 1)
    print(hex(totient))
    inverse = uclid(descKey, totient)
    encrypt = pows(N, messagehash, inverse)
    decrypt = pows(N, encrypt, descKey)
    print(hex(encrypt))
    print(hex(decrypt))
    return


def rsaverify(N, message, sig):
    return


# def rsa():
#     data = input()
#     args = data.split()
#     if(len(args) <2):
#         print("invalid arguments")
#         return
#     if(len(args) <3):#sign
#         if(data[0] != "sign"):
#             print("invalid input")
#             return
#         print("sign starting")
#         rsasign(data[1])
#         return
#     elif(len(args)<4):#verify
#         if(data[0]!= "verify"):
#             print("invalid input")
#             return
#         print("verify starting")
#         rsaverify(data[1], data[2], data[3])
#         return
def rsa():
    rsasign("hello, friend!")


rsa()
