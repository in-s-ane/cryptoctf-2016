from PIL import Image

flag = ""

BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 0)

## PART 1

image = Image.open("blind/part1.png")
pixels = image.load()
width, height = image.size
diff = Image.new("RGB", (width, height))
diff_pixels = diff.load()

for x in range(width):
    for y in range(height):
        pixel = pixels[x, y]
        if pixel != BLACK:
            diff_pixels[x, y] = WHITE
        else:
            diff_pixels[x, y] = BLACK

diff.save("blind/part1-solution.png")
flag += "flag{look_to"

## PART 2

image = Image.open("blind/part2.png")
pixels = image.load()
width, height = image.size

diff = Image.new("RGB", (width, height))
diff_pixels = diff.load()

for x in range(width):
    for y in range(height):
        pixel = pixels[x, y]
        if pixel != BLACK:
            diff_pixels[x, y] = WHITE
        else:
            diff_pixels[x, y] = BLACK

diff.save("blind/part2-solution.png")
flag += "_the_right_to_fi"

## PART 3

image = Image.open("blind/part3.png")
pixels = image.load()
width, height = image.size

diff = Image.new("RGB", (width, height))
diff_pixels = diff.load()

for x in range(width):
    for y in range(height):
        pixel = pixels[x, y]
        if pixel != BLACK:
            diff_pixels[x, y] = WHITE
        else:
            diff_pixels[x, y] = BLACK

diff.save("blind/part3-solution.png")
flag += "nd_tHree_Do"

## PART 4
# $ strings part4.png | grep "}"

flag += "ts_dARn_gk}"

print flag

# This problem is a reference to a little thing that went on the EasyCTF slack with gengkev
# The first three problems are to purely get you used to looking for information in the pixels,
# but the last problem is just a string in the png.

# flag{look_to_the_right_to_find_tHree_Dots_dARn_gk}
