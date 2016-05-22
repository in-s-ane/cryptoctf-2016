from math import floor

enc = open("encrypted.dat", "r").readlines()

lengths = [len(line.strip()) for line in enc]
print lengths
l1 = [chr(int(floor(len(line.strip())*3.35))) for line in enc]
print "".join(l1)
l2 = [chr(ord(x)+1) for x in l1]
print "".join(l2)
l3 = [chr(ord(x)+2) for x in l1]
print "".join(l3)
l4 = [chr(ord(x)-1) for x in l1]
print "".join(l4)
l5 = [chr(ord(x)-2) for x in l1]
print "".join(l5)
l6 = [chr(ord(x)-3) for x in l1]
print "".join(l6)

# Definitely not the intended solution, but hey, it worked.
# Multiply the lengths of each line by a certain factor, knowing that the first 5 characters correspond to "flag{" and the last character corresponds to "}"
# Play around with the offsets and piece together the flag:
# flag{i_liked_the_f1rst_on3_better_shouts_to_sctf}
