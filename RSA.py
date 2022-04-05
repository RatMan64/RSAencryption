#Riley Barnes
#cs427
#Python3

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


def pows():

    return
def elfhash(s):
    h = 0
    high = 0
    for i in s:
        h = (h <<4) + s
        high = h & int("F0000000", 16)
        if(high):
            h ^= high >> 24
        h &= ~high

    return h
def uclid(a, n):
    t = 0
    r = n
    newt = 1
    newr = a
    while newr != 0:
        quotient = r/newr
        t, newt = (newt, t - quotient*newt)
        r , newr = (newr, r- quotient*newr)

    if(r>1):
        return -1
    if( t< 0):
        t = t+n
    return t

def rsasign(message):

    messagehash = elfhash(message)

    p = int(testp,16)
    q = int(testq,16)
    N = q * p
    tocient = (q-1)*(p-1)
    inverse = uclid(descKey, tocient)
    encrypt = pows()
    decrypt = pows()
    return
def rsaverify(N, message, sig):

    return
def rsa():
    data = input()
    args = data.split()
    if(len(args) <2):
        print("invalid arguments")
        return
    if(len(args) <3):#sign
        if(data[0] != "sign"):
            print("invalid input")
            return
        print("sign starting")
        rsasign(data[1])
        return
    elif(len(args)<4):#verify
        if(data[0]!= "verify"):
            print("invalid input")
            return
        print("verify starting")
        rsaverify(data[1], data[2], data[3])
        return
rsa()