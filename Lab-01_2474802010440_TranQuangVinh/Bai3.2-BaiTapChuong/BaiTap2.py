#Bai02:
from sympy import Symbol, solve,I
#1
print("1. PHƯƠNG TRÌNH CÓ NGHIỆM THỰC:")
x = Symbol('x')
pt1 = x**2 + 9*x + 8
nghiem1 = solve(pt1, x, dict=True)
print(f"Phương trình x² + 9x + 8 = 0 có nghiệm: {nghiem1}")
#2
print("\n2. PHƯƠNG TRÌNH CÓ NGHIỆM PHỨC:")
pt2 = x**2 + x + 10
nghiem2 = solve(pt2, x, dict=True)
print(f"Phương trình x² + x + 10 = 0 có nghiệm: {nghiem2}")