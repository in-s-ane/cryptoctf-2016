enc = open("threefold", "r").read().strip()

while "flag{" not in enc:
    enc = enc.decode("hex")

print enc

# Continuously decode the hex until we get the flag
# flag{everything's_better_in_groups_of_three}
