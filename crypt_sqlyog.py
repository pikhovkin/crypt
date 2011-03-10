# -*- coding: utf-8 -*-

from base64 import encodestring, decodestring


def RotateBitRight(password):
    return ''.join(
        [chr(((ord(c) >> 1) | (ord(c) << 7)) & 255) for c in password])

def RotateBitLeft(password):
    return ''.join(
        [chr(((ord(c) << 1) | (ord(c) >> 7)) & 255) for c in password])

def DecodePassword(password):
    return RotateBitLeft(decodestring(password)).strip()

def EncodePassword(password):
    return encodestring(RotateBitRight(password)).strip()
