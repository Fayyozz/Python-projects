import random


def election_check(win_rate):
    real_rate = random.random()
    if real_rate < win_rate:
        return True
    else:
        return False


resultA = 0
for _ in range(10_000):
    region1 = election_check(0.87)
    region2 = election_check(0.65)
    region3 = election_check(0.17)
    if (region1 + region2 + region3) >= 2:
        resultA = resultA + 1

print(f" Probability that A wins -> {resultA / 10_000:.2f}")

