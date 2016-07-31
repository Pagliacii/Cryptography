#!/usr/bin/env python
#_*_ coding : utf-8 _*_
# author : jason huang
# version : 1.0

def plain2ascii(plain):
    # 将明文转换为 ASCII 码
    ascii_list = []
    for i in plain:
        ascii_list.append(ord(i))
    return ascii_list

def ascii2binary(_ascii):
    # 将 ASCII 码转换为二进制数
    binary_list = []
    for i in _ascii:
        binary_list.append(bin(int(i)))
    return binary_list

def binary2ascii(binary):
    # 将二进制数转换为 ASCII 码
    # 由于 ASCII 码中只有 32 到 126 属于可显示字符
    # 所以将之范围约束在 32 - 126
    text = ''
    for i in binary:
        asciinum = int(i, 2)
        if asciinum < 32:
            asciinum += 32
        elif asciinum > 126:
            asciinum -= 126
        
        text = text + chr(asciinum)

    return text

def binformat(num):
    # 将二进制数统一为 8 位格式
    formation = []
    for i in num:
        i = i.split('b')[1]
        l = len(i)
        if l < 8:
            formation.append('0' * (8-l) + i)
    
    return formation

def encrypt(plain, keyword):
    # 异或
    result = []
    temp = ''
    for i in range(len(plain)):
        result.append(bin(int(plain[i]) ^ int(keyword[i])))

    for j in result:
        temp = temp + j[-1]

    return temp

def encryptloop(plaintext, keywords):
    # 批量异或
    ciphernumber = []
    for i in range(len(plaintext)):
        ciphernumber.append(encrypt(plaintext[i], keywords[i]))

    return ciphernumber

def createkeys(save=False):
    # 生成 128 位密钥，并分为 16 个 8 位二进制数
    import random as r
    keybit = []
    key = bin(r.randrange(2**64, 2**128))
    key = key.split('b')[1]
    if len(key) < 128:
        l = 128 - len(key)
        key = '0' * l + key

    for x in range(len(key)):
        if x % 8 == 0:
            keybit.append(key[x:x+8])

    if save:
        record('keywords.json', keybit)

    return keybit

def createciphertext(plaintext, keywords):
    # 调用上面的函数，生成密文
    p2a = plain2ascii(plaintext)
    a2b = ascii2binary(p2a)
    bformat = binformat(a2b)
    temp = encryptloop(bformat, keywords)
    ciphertext = binary2ascii(temp)

    return ciphertext