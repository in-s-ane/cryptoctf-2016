lines = open("mlg_crypto.txt", "r").readlines()[1:-1]
subs = {}

for line in lines:
    line = line.strip()
    for word in line.split("_"):
        if word in subs:
            subs[word] += 1
        else:
            subs[word] = 1

print len(subs)
print subs
space = max(subs, key=lambda x: subs[x])
del subs[space]

total = "\n".join(lines)
total = total.replace(space, " ") # Most common character is " "

# Do some bs substitutions
alphabet = "abcdefghijklmnopqrstuvwxyz"
i = 0
for sub in subs:
    total = total.replace(sub, alphabet[i])
    i += 1

total = total.replace("_", "").replace("\n\n", "\n")
print total

# Given the hint, we need to crack the substitution cipher on the ciphertext.
# This script will assign each word a letter and print it out
# Plugging the output into quipqiup, we kinda decode the message and the flag:

# flag{leet_smoked_memes_bro}
