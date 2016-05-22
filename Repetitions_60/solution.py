from itertools import cycle, izip

def xor(msg, key):
    return ''.join(chr(ord(c)^ord(k)) for c,k in izip(msg, cycle(key)))

enc = open("repetitions.txt", "r").read().strip()
enc = enc.decode("hex")

for key in range(256):
    candidate = xor(enc, chr(key))
    if "flag{" in candidate:
        print "Key: %s" % hex(key)
        print "Message: %s" % candidate

# Given the name of the problem, we can assume that we are dealing with a repeated xor cipher.
# Given the problem point value and the fact that many characters are repeated, we can also assume
# that the key length is 1. Knowing this, we can brute force all possible keys to decrypt the ciphertext.

# Solving repeating xor ciphers is easy when there is only one byte. flag{X0r_4ga1n_n_4ga1n}
