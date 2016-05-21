enc = open("wut", "rb").read()

characters = {}
for char in enc:
    if char in characters:
        characters[char] += 1
    else:
        characters[char] = 1

common = max(characters, key=lambda i: characters[i])
print "The most common character is %s" % common.encode("hex")
print "Expected \\x00"

dec = ""

for char in enc:
    tmp = ord(char) - ord(common)
    if tmp < 0:
        tmp += 0xff
    dec += chr(tmp)

open("dec.7z", "wb").write(dec)

# The most common character in a file is \x00, but in this file, the most common character is \x0d
# The difference between the two characters is 13, so let's just shift each character in the encrypted
# file by 13. We get a 7z archive, which when unzipped gives the flag.

# flag{1_c4n_ROT13_f1l3z_t00}
