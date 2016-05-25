from decimal import Decimal

def gcd(*numbers):
    from fractions import gcd
    return reduce(gcd, numbers)

def lcm(*numbers):
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers, 1)

ciphertexts = [25320377978421626271037739018425661814332530641734365195520598688669147974626,
               51049728329675544602468883246195883243178220099348551042093609387772659562715,
               48969665638425896697720681354040354035528713671547018252651937200345154154498,
               20487080364262701406592929679213809564572680718344769353109544343384535019350,
               3427300824030705432360313320478215252474992494622007646771780714090551587321,
               21530290667542576868576875394108654770812594313730275587484522325710519111513,
               22683911662231624218695323236646155262304075667861840937064677419948597164544]

N = 59343067093100802875412193056951771037923087891901784812862982338317968795059
p = 16042325824659068983
q = 230587267661588072064667605796004068931

assert p**2 * q == N

flag = ""

# d = (1.0 / N) % (lcm(p-1, q-1))
d = 1564702757571922808162498222313865178315063430963230526749

i = 0
# decrypted using m = c^d mod pq
for dec in [1718378855, 2071159656, 1835623540, 1601397101, 1868652393, 1935631152, 7302269]:
    assert ciphertexts[i] == pow(dec, N, N)
    i += 1
    flag += hex(dec)[2:]

print flag.decode("hex")

# Looking at the hint, I guessed that the encryption method used was related to a Girl Scout Cookie. Looking at the
# list of cookies that Girl Scouts sell, combined with the previous hint about coconuts, I guessed that the cryptosystem used
# is Schmidt-Samoa (https://en.wikipedia.org/wiki/Schmidt-Samoa_cryptosystem). Similar to RSA, it uses a public key to encrypt, and a private key to decrypt.
# Each ciphertext corresponds to a chunk of the plaintext, which we can combine to get the actual flag:

# flag{schmidt_samoa_is_c0ol}
