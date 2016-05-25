_file = "psychic3/psychic3_%s.lol"

lines = []

for x in range(54):
    lines.append(open(_file % x, "r").read().strip())

sums = []

for x in range(len(lines[0])):
    _sum = 0
    for line in lines:
        _sum += int(line[x])
    sums.append(_sum)

print "".join(chr(char) for char in sums)

# Take the sum of the columns of the ciphertext and turn the numbers into their
# respective ascii characters to decode the message:

# now i'm too lazy to even come up with a message to keep the flag in whoops it's 12:18 AM flag{never_make_problems_after_midnight}
