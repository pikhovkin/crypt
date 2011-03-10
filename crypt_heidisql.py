# -*- coding: utf-8 -*-

def encrypt(password):
    from random import randrange
    result = ''
    salt = randrange(1, 10)
    for c in password:
        nr = ord(c) + salt
        if nr > 255:
            nr -= 255
        h = hex(nr)[2:]
        if len(h) == 1:
            h = '0'.join(h)
        result += h

    return result + str(salt)

def decrypt(password):
    if not password:
        return ''

    try:
        salt = int(password[-1])
    except ValueError:
        salt = 0

    result = ''
    i = 0
    n = len(password) - 1
    while i < n:
        nr = int(float.fromhex(''.join(['0x', password[i:i + 2]]))) - salt
        if nr < 0:
            nr += 255
        result += chr(nr);
        i += 2

    return result
