#!/usr/bin/env python3
#_*_ coding : utf-8 _*_
# author : jason huang
# version: 1.0

import random

letters = 'abcdefghijklmnopqrstuvwxyz'
lowerletters = [x for x in letters]
upperletters = [x.upper() for x in letters]

def createtable(letter):
    table = []
    for i in range(len(letter)):
        table.append(letter.pop(random.randrange(len(letter))))

    return table

def encrypts(plaintext, table):
    ciphertext = ''
    for p in plaintext:
        ciphertext = ciphertext + table[lowerletters.index(p)]

    return ciphertext

def decrypts(ciphertext, table):
    plaintext = ''
    for c in ciphertext:
        plaintext = plaintext + lowerletters[table.index(c)]

    return plaintext
