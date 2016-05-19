mappings = open("message", "r").readlines()
preamble = open("Preamble", "r").readlines()

flag = ""

for mapping in mappings:
    mapping = mapping.split(",")
    line = int(mapping[0])
    word = int(mapping[1])
    character = int(mapping[2])

    flag += preamble[line].split(" ")[word][character]

print flag

# The image contains a hidden zip, and if we extract it, we are given two new files, message and Preamble
# Immediately, we can assume that it is some sort of poem cipher, using the preamble as the poem.
# The three items in each line in message are the line, word, and character of the flag.
# For example, 1,5,10 would mean the first line, fifth word, and tenth character. Except not really
# because the count starts from zero.

# Putting the flag in the proper format:
# flag{Ohsaycanyousee}
