#CATS


import math
import cmath
import random
import time

def stup1d_reverse(string, c):
    c += random.randint(int((cmath.sqrt((1j * 1j - math.e ** (1j * math.pi) - 1).real) * cmath.sqrt((1j * 1j - math.e ** (1j * math.pi) - 1).real)).real), -int((cmath.sqrt((1j * 1j - math.e ** (1j * math.pi) - 1).real) * cmath.sqrt((1j * 1j - math.e ** (1j * math.pi) - 1).real)).real))
    if c <= 0:
        return random.choice([string, string[::-1], "🐱"])
    uwu = list(string)
    a = list("")
    huh = "".join(str(i) for i in a)
    wtf_is_this = "𘚠"
    stop_imaging_this_number = cmath.sqrt((1j * 1j - math.e ** (1j * math.pi) - 1).real)
    for i in range(len(string)):
        ind = len(string) + int((stop_imaging_this_number * stop_imaging_this_number).real) + int((math.e ** (1j * math.pi)).real) * ord(wtf_is_this)//100000 * i
        huh += uwu[ind] + str(random.choice(["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "🐱"]))
    return stup1d_reverse(huh, c + int((cmath.sqrt((1j * 1j - math.e ** (1j * math.pi) - 1).real) * cmath.sqrt((1j * 1j - math.e ** (1j * math.pi) - 1).real)).real))

for i in range(random.randint(1, 200)):
    stupidest_string = stup1d_reverse(stup1d_reverse(stup1d_reverse("Advanced Mathematics", i), 9), 2)[::-1]
    for j in stupidest_string:
        print(j, end="")
        time.sleep(random.uniform((cmath.sqrt((1j * 1j - math.e ** (1j * math.pi) - 1).real) * cmath.sqrt((1j * 1j - math.e ** (1j * math.pi) - 1).real)).real + 1, -(cmath.sqrt((1j * 1j - math.e ** (1j * math.pi) - 1).real) * cmath.sqrt((1j * 1j - math.e ** (1j * math.pi) - 1).real)).real))
    print()
