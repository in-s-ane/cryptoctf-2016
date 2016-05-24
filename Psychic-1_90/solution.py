import string

def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

def prime(i, primes):
    for prime in primes:
        if not (i == prime or i % prime):
            return False
    primes.add(i)
    return i

def gen_primes(n):
    primes = set([2])
    i, p = 2, 0
    while True:
        if prime(i, primes):
            p += 1
            if p == n:
                return primes
        i += 1

enc = open("decryptme", "r").read().strip().lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"

dec = ""
primes = sorted(list(gen_primes(len(enc))))

enc = zip(enc, primes)

for char, shift in enc:
    if char in alphabet:
        dec += caesar(char, 26 - (shift % 26))
    else:
        dec += char

print dec

# Despite the problem stating that there are no hints in the description, we know that the ciphertext likely begins with "Sorry"
# Looking at the shifts, it becomes clear that the plaintext was shifted by prime numbers.
# Just undo the shift to decode the message:

# sorry, sometimes problem statements are difficult to come up with. this seemed like an easy way out. the flag is flag{color_by_numbers_and_rot_by_primes}
