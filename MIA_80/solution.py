flag = ""

key = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

for x in range(46):
    _file = "file%s.txt" % x
    enc = open(_file, "r").read().split()

    missing = enc.index("*")
    flag += key[missing]

print flag.decode("hex")

# Each of the text files has a character replaced with a star. If we take all the characters that are
# "MIA", we can piece together the hex encoded version of the flag. Decode the hex to get the actual flag:

# flag{m1Ss1ng_1N_4cT10n}
