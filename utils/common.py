#!usr/bin/env python
#-*- coding:utf-8 -*-

import hashlib


def hash_code(s, salt='young'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def md5(s, raw_output=False):
    """Calculates the md5 hash of a given string"""
    res = hashlib.md5(s.encode())
    if raw_output:
        return res.digest()
    return res.hexdigest()