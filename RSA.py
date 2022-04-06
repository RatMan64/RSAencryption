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
        d = d // 2
    while (k > 0):
        a = random.randrange(2, n-2)
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
        high = h & 0xF0000000
        if (high):
            h ^= high >> 24
        h &= (0xFFFFFFFF^high)
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
    message = message.strip('"')
    messagehash = elfhash(message)


    p = int(testp, 16)
    q = int(testq, 16)
    # p = random.randint(int("8000",16), int("FFFF",16))
    # while(prime(p,20)!= 1):
    #     p = random.randint(int("8000",16), int("FFFF",16))
    # q = random.randint(0,65535)
    # while prime(q,20) != 1:
    #     q = random.randint(0, 65535)


    N = q * p
    # print(hex(N))
    totient = (q - 1) * (p - 1)
    print(f"p= {hex(p)[2:]}, q= { hex(q)[2:]}, n= {hex(N)[2:]}, t= {hex(totient)[2:]}"  )
    print("received message: %s"% message)
    print("message hash:%s" % hex(messagehash)[2:])

    inverse = uclid(descKey, totient)
    print("signing with the following private key: %s" % hex(inverse)[2:])
    encrypt = pows(N, messagehash, inverse)
    print("signed hash: %s" % hex(encrypt)[2:])
    decrypt = pows(N, encrypt, descKey)
    print("uninverted message to ensure integrity: %s" % hex(decrypt)[2:])
    print(f"complete output for verification:\n{hex(N)[2:]} '{message}' {hex(encrypt)[2:]}" )

    return


def rsaverify(N, message, sig):
    message = message.strip('"')
    messagehash = elfhash(message)
    decrypt = pows(int(N,16),int(sig,16),descKey )
    if(messagehash == decrypt):
        print("message verified!")
        return
    print("!!! message is forged !!!")
    return


def rsa():
    data = input()
    args = data.split()

    if(len(args) ==2):#sign
        if(args[0] != "sign"):
            print("invalid input")
            return
        print("sign starting")
        rsasign(args[1])
        return
    elif(len(args)==4):#verify
        if(args[0]!= "verify"):
            print("invalid input")
            return
        print("verify starting")
        rsaverify(args[1], args[2], args[3])
        return



rsa()
