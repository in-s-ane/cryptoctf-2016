enc = "caecbdbggcafcdeccecagcadbgeccdcbgccfcbfcacbgecbgcaebgecabccccdcccaccecbgcafcccbggccacagcbacabbgecbecdcccdccecadccccdccdg"

def chunks(l, n):
    n = max(1, n)
    return [l[i:i + n] for i in range(0, len(l), n)]

enc = enc.replace("a", "0").replace("b", "1").replace("c", "2").replace("d", "3").replace("e", "4").replace("f", "5").replace("g", "6")
enc = chunks(enc, 3) # Split into chunks of 3 because each measure had 3 notes

print "".join([chr(int(x, 7)) for x in enc])

# Looking at the pdf, we find a lot of musical notes, with each measure containing 3 notes.
# Taking a as 0, b as 1, c as 2, etc, we can turn the letters into numbers.
# Looking at the hint, we can deduce that each number represented by each measure is in base 7,
# so convert to decimal and print out the characters represented by each ascii value.

# flag{the_sound_of_cryptographic_mystery}
