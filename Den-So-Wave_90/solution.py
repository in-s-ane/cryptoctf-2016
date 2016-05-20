from PIL import Image, ImageDraw

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

qr = open("den_so_wave.txt", "r").read().strip()

height, width = (150, 150)

image = Image.new("RGB", (height, width))
pixels = image.load()

pos = 0 # position in qr string
for x in range(width):
    for y in range(height):
        pixels[x, y] = [BLACK, WHITE][qr[pos] == "0"]
        pos += 1

image.save("qr.png")

# Looking up the name of the problem, we find something about a company called Denso Wave, which created the two dimensional qr code.
# We also find out that the length of the binary string is a perfect square, so we can deduce that we need to generate a qr code from this.

# Scan the qr code to get the flag:
# flag{qlever_binary_qryptography}
