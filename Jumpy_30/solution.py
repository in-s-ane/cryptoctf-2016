enc = "ewt 0ei5wrsk 5 iyffl00llurae tgdmeo uhpcswettenf 3b3bnrreca! lc qoetussh1eketb1 erpf alltceahetg"

print "".join([enc[x] for x in range(0, len(enc), 4)])
print "".join([enc[x] for x in range(3, len(enc), 4)])
print "".join([enc[x] for x in range(2, len(enc), 4)])
print "".join([enc[x] for x in range(1, len(enc), 4)])

# There's probably a better way to do this:
# flag{sk1pletter5f0rtehw3n}
