import math, cmath, random, time
def 嬩笘鐣屼笂鏈(閫欐槸涓, 鍊):
    鍊 += random.randint(int((cmath.sqrt((1j * 1j - math.e ** (1j * math.pi) - 1).real) * cmath.sqrt((1j * 1j - math.e ** (1j * math.pi) - 1).real)).real), -int((cmath.sqrt((1j * 1j - math.e ** (1j * math.pi) - 1).real) * cmath.sqrt((1j * 1j - math.e ** (1j * math.pi) - 1).real)).real))
    if 鍊 <= 0:
        return random.choice([閫欐槸涓, 閫欐槸涓[::-1], "🐱"])
    鐨凱 = "".join(str(i) for i in list(""))
    鎴戞槸鍌婚 = "🐱"
    for 鍌婚 in range(len(閫欐槸涓)):
        鎴戞 = len(閫欐槸涓) + int((cmath.sqrt((1j * 1j - math.e ** (1j * math.pi) - 1).real) * cmath.sqrt((1j * 1j - math.e ** (1j * math.pi) - 1).real)).real) + int((math.e ** (1j * math.pi)).real) * ord(鎴戞槸鍌婚)//128049 * 鍌婚
        鐨凱 += list(閫欐槸涓)[鎴戞] + str(random.choice(["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "🐱"]))
    return 嬩笘鐣屼笂鏈(鐨凱, 鍊 + int((cmath.sqrt((1j * 1j - math.e ** (1j * math.pi) - 1).real) * cmath.sqrt((1j * 1j - math.e ** (1j * math.pi) - 1).real)).real))

闆ｉ柋璁 = 嬩笘鐣屼笂鏈(嬩笘鐣屼笂鏈(嬩笘鐣屼笂鏈("Advanced Mathematics", 8), 9), 2)[::-1]
for 槸 in 闆ｉ柋璁:
    print(槸, end="")
    time.sleep(random.uniform((cmath.sqrt((1j * 1j - math.e ** (1j * math.pi) - 1).real) * cmath.sqrt((1j * 1j - math.e ** (1j * math.pi) - 1).real)).real + 1, -(cmath.sqrt((1j * 1j - math.e ** (1j * math.pi) - 1).real) * cmath.sqrt((1j * 1j - math.e ** (1j * math.pi) - 1).real)).real))
print()
