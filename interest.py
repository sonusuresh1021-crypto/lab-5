import sys

def calculate_si(p, r, t):
    si = (p * r * t) / 100
    print("Simple Interest =", si)

p = float(sys.argv[1])
r = float(sys.argv[2])
t = float(sys.argv[3])

calculate_si(p, r, t)
