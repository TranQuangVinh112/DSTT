#Bai01:
from sympy import Symbol, solve
x = Symbol('x')
# Pt 1:
bieuthuc1 = x + 3 - 5
nghiem1 = solve(bieuthuc1)
print("Nghiệm phương trình x + 3 - 5 = 0:", nghiem1)  
# Pt2
bieuthuc2 = x**2 + 3 - 5
nghiem2 = solve(bieuthuc2)
print("Nghiệm phương trình x^2 + 3 - 5 = 0:", nghiem2)  
print("Nghiệm thứ nhất của phương trình 2:", nghiem2[0])  
print("Nghiệm thứ hai của phương trình 2:", nghiem2[1])   
