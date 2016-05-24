from PIL import Image

image = Image.open("spiral.png").convert("RGB")
pixels = image.load()
width, height = image.size

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
visited = []

def is_valid(x, y):
    global visited
    if 0 <= x < width and 0 <= y < height:
        return pixels[x, y] != BLACK and (x, y) not in visited
    return False

def get_next(x, y):
    if is_valid(x+1, y):
        return x+1, y
    elif is_valid(x-1, y):
        return x-1, y
    elif is_valid(x, y+1):
        return x, y+1
    elif is_valid(x, y-1):
        return x, y-1

def traverse(x, y):
    global visited
    pixel_list = []
    pixel = pixels[x, y]
    while pixel != WHITE:
        visited.append((x, y))
        mean = sum(list(pixel)) / len(pixel)
        pixel_list.append(mean)
        x, y = get_next(x, y)
        pixel = pixels[x, y]
    return pixel_list

pixel_list = traverse(0, 0)
message = "".join([chr(char) for char in pixel_list])
message = message[::-1] # Oops, I read the pixels the wrong way...
print messsage[message.find("flag{"):message.find("}")+1]

# Read off the pixels in a spiral like fashion. The correct way was to read from the center and spiral out, but
# this program reads from the top left and spirals inward. Take the *mean* of all the RGB values for each pixel, and
# convert the resulting numbers into their respective ascii characters.

# flag{that_was_average}
