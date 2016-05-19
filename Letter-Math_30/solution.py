enc = open("letter_math.txt", "r").readlines()

dec = ""

for line in enc:
    dec += chr(eval(str(ord(line[0])) + line[1:3]))

print dec

# Take the characters given in the ciphertext, and increment/decrement appropriately.
# flag{L3tt3rz_R_Num63rz_2}
