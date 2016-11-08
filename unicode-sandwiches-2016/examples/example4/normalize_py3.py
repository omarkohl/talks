#!/usr/bin/env python3

def compare(s1, s2):
    print("\n")
    print("s1 = %s" % s1)
    print("s2 = %s" % s2)
    print("len(s1): %s" % len(s1))
    print("len(s2): %s" % len(s2))
    print("s1 == s2: %s" % (s1 == s2))


s1 = 'café'
s2 = 'cafe\u0301'  # combining character

compare(s1, s2)


# Solution

from unicodedata import normalize

s1_nfc = normalize('NFC', s1)
s2_nfc = normalize('NFC', s2)

compare(s1_nfc, s2_nfc)

s1_nfd = normalize('NFD', s1)
s2_nfd = normalize('NFD', s2)

compare(s1_nfd, s2_nfd)
