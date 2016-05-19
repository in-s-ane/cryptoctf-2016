enc = open("txt.txt", "r").read()

print "".join([chr(ord(x)/2) for x in enc])

# flag{just_another_ASCII_cipher}
