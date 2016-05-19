enc = open("so_many", "r").read()
dec = enc.replace("dftjizvcnalyprgobkqwsxeuhm", "")
print dec

# There are strings put in between the different characters of the flag. Remove them to get the flag.
# flag{r3peating_over_and_0ver_and_ov3r_and_0v3r}
