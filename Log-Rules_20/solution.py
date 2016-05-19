enc = open("log_rules.txt", "r").read().strip().split("-")

enc = "".join([chr(int(x, 8)) for x in enc]) # Decode from base 8
enc = enc.decode("base64") # Decode from base 64
enc = enc.decode("hex") # Decode from hex (base 16)
print enc

# flag{basically_brandon_mccartney}
