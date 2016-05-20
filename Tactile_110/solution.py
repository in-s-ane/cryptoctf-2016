from PIL import Image

pixel_multiplier = 5 # Each block is 5 pixels

braille = {
    "000000": " ",
    "100000": "A",
    "101000": "B",
    "110000": "C",
    "110100": "D",
    "100100": "E",
    "111000": "F",
    "111100": "G",
    "101100": "H",
    "011000": "I",
    "011100": "J",
    "100010": "K",
    "101010": "L",
    "110010": "M",
    "110110": "N",
    "100110": "O",
    "111010": "P",
    "111110": "Q",
    "101110": "R",
    "011010": "S",
    "011110": "T",
    "100011": "U",
    "101011": "V",
    "011101": "W",
    "110011": "X",
    "110111": "Y",
    "100111": "Z"
}

n = 0
dec = ""

for x in range(960):
    print "Analyzing image %s" % x
    image = Image.open("images/tactile-%03d.png" % x)
    pixels = image.load()
    binary = ""
    for y in range(3):
        for x in range(2):
            pixel = pixels[x*pixel_multiplier,y*pixel_multiplier]
            binary += ["0", "1"][pixel == 0]

    try:
        dec += braille[binary]
    except:
        # Unexpected, but we'll let it slide ;)
        pass

print dec

# The name of the problem suggests that we are dealing with braille, and a few manual decryptions reveals that it is
# The problem now is decrypting each and every character. There's probably a better way, and for some reason all the B's come out as V's.
# $ convert tactile.png -crop 10x15 images/tactile-%03d.png

# flag{eulerwasanintegralpartofmathematics}
