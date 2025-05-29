#Bai03:
print("\n1. Khai báo biến và phương trình:")
from sympy import Symbol, solve, pprint
# Định nghĩa các biến symbol
x = Symbol('x')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
ptb2 = a*x**2 + b*x + c
nghiem = solve(ptb2, x, dict=True)
print("Nghiệm tổng quát của phương trình bậc 2 a*x^2 + b*x + c = 0:")
pprint(nghiem)
