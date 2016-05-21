import hashlib
import string

alphabet = string.ascii_letters + string.digits + string.punctuation
rainbow = {}
for char in alphabet:
    hashed = hashlib.md5(char).hexdigest()
    rainbow[hashed] = char

key = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'][::-1]

_all = ""
for x in range(768):
    _file = "file%s.txt" % x
    enc = open(_file, "r").read().split()

    missing = enc.index("*")
    _all += key[missing]

flag = ""
for x in range(0, len(_all), 32):
    flag += rainbow[_all[x:x+32]]

print flag

# Given the hint, we can assume that we need to take the missing characters 32 at a time.
# What strings are made up of 32 hex characters? MD5 hashes.
# Each md5 hash represents 1 character of the flag, so we can just create a rainbow table and
# look up each hash individually.

# flag{m1ssing_y3t_4ga1n?}
