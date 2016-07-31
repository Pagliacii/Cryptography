#!/usr/bin/env python3
#_*_ coding : utf-8 _*_
# author : jason huang
# version: 1.0

import time, os, json
from CaesarCipher import *
from OneTimePad import *
from SimpleSubstitutionCipher import *

keywords = './keywords'
keytables = './keytables'
ciphertexts = './ciphertexts'

def save(filename, content):
    with open(filename, 'a') as f:
        json.dump(content, f)

def savefile(content, keydir, times=3):
    while times > 0:
        currentdate = time.strftime('%y%m%d', time.localtime(time.time()))
        currenttime = time.strftime('%H%M%S', time.localtime(time.time()))
        
        if not os.path.exists(keydir):
            os.mkdir(keydir)
        if not os.path.exists(keydir + '/' + currentdate):
            os.mkdir(keydir + '/' + currentdate)
        
        filename = keydir + '/' + currentdate + '/' + currenttime + '.json'
        save(filename, content)
        times = times - 1

        if not os.path.isfile(filename):
            continue
        else:
            return None

    print('The contents can not save as file!')
    return None

def main():
    plaintext = input('Please enter the plaintext: ')
    if not plaintext.isalpha():
        return None

    method = menu()
    while True:
        if method == '1':
            key = 0
            while True: 
                key = input('Please enter a number as a key(0 - 25): ')
                if key.isdigit():
                    break
                else:
                    continue

            ciphertext = Caesarcipher(plaintext, int(key), 'encrypt')
            break
        elif method == '2':
            keytable = createtable(upperletters)
            ciphertext = encrypts(plaintext, keytable)
            break
        elif method == '3':
            key = createkeys()
            ciphertext = createciphertext(plaintext, key)
            break
        elif method == '0':
            return None
        else:
            print('Input Error!\n')
            method = menu()
            continue

    print('Your ciphertext is %s' % ciphertext)
    
    savecipher = input('Do you want to save ciphertexts?(y/n): ')
    if savecipher == 'y':
        savefile(ciphertext, ciphertexts)
    
    if method == '2':
        savetable = input('Do you want to save the substitution table?(y/n): ')
        if savetable == 'y':
            savefile(keytable, keytables)

    if method == '3':
        savetable = input('Do you want to save the key?(y/n): ')
        if savetable == 'y':
            savefile(key, keys)

    return None

def menu():
    print('''
================ Menu ================
|   1. Caesar Cipher                 |
|   2. Simple Substitution Cipher    |
|   3. One Time Pad                  |
|   0. Exit                          |
======================================
        ''')

    method = input('Please select a encryption method: ')
    return method

if __name__ == '__main__':
    main()