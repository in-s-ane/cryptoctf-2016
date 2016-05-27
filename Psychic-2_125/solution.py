_file = "psychic_2_files/psychic2_%s.lol"

dec = ""
for x in range(91):
    fin = open(_file % x, "r").read().strip()
    fin = fin.decode("hex")
    xor = ord(fin[0])
    for i in range(1, len(fin)):
        xor ^= ord(fin[i])
    dec += chr(xor)

print dec

# Each file represents one character in the plaintext, and given the hint, we can guess that we probably
# need to xor all the characters in each file to get the characters of the plaintext:
# in the spirit of psychic problems, here's a Caesared flag: pvkq{e_bokn_wi_wsxn_agbslsfigso}

# Caesar shift the flag by 10 to decode the flag:
# flag{u_read_my_mind_qwribivywie}
