#Đặt nhân tử chung và khai triển biểu thức 
from sympy import symbols, factor, expand
x, y = symbols('x y')
bieuthuc1 = x**3 - y**3
ketqua_factor = factor(bieuthuc1)
print("Biểu thức sau khi factor(x**3 - y**3):", ketqua_factor)
bieuthuc2 = (x - y)*(x**2 + x*y + y**2)
ketqua_expand = expand(bieuthuc2)
print("Biểu thức sau khi expand((x - y)(x^2 + xy + y^2)):", ketqua_expand)
bieuthuc3 = x**3 - y**3
print("Gọi expand trên biểu thức đã expand:", expand(bieuthuc3))
