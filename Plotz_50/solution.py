import matplotlib.pyplot as plot

points = open("plotz.txt", "r").readlines()
x = []
y = []
for point in points:
    coords = point.strip().split(",")
    x.append(coords[0])
    y.append(coords[1])

plot.plot(x, y, "ro")
plot.axis([0, 200, -10, 70])
plot.show()

# Just plot the points given in the text file and read out the flag:
# flag{c0nn3ct_th3_d0tz}
