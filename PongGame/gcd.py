
def gcd(p, q):
    if q == 0:
        return p
    r = p % q
    return gcd(q, r)

print(gcd(18, 12))

