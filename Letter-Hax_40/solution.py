enc = "241 166 { 67 161 _ 192 255 238 _ 21 _ 80 _ 19 55 }"
enc = enc.split(" ")

dec = ""

for char in enc:
    try:
        char = hex(int(char))[2:]
    except:
        pass
    dec += char

print dec

# Considering that the first two numbers correspond to "flag", we can guess that each number
# represents two characters. Converting each number into hex, we can make out most of the flag:
# f1a6{43a1_c0ffee_15_50_1337}

# Only the last word of the actual is leetified, so we get the following:
# flag{real_coffee_is_so_1337}
