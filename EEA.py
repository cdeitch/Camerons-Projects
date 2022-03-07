print("input two numbers you would like to find GCD for:")
x, y = int(input()), int(input())


def eea(a, b):
    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = b
    old_r = a
    while r != 0:
        q = old_r // r
        rtemp = r
        r = old_r - q * r
        old_r = rtemp
        stemp = s
        s = old_s - q * s
        old_s = stemp
        ttemp = t
        t = old_t - q * t
        old_t = ttemp
    print(f"GCD={old_r}")
    return t, s


w, v = eea(x, y)
print(w, x)
