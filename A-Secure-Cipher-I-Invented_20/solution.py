enc = open("super_secure.txt", "r").readline()

print "".join([chr(int(x)) for x in enc.split(" ")])

# We are given the ascii character codes of the characters representing the flag.
# Convert the codes to their corresponding characters to get the flag:

# flag{shouts_out_to_zascii}
