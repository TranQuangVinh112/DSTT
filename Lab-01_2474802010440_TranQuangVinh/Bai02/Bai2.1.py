#Định nghĩa Symbol và các phép toán hình thức (symbolic)
from sympy import Symbol, symbols
# Tạo một symbol đơn lẻ
x = Symbol('x')
f = x + x + x + 2
print("Biểu thức f = x + x + x + 2:", f)  # 3*x + 2
# Tạo biểu thức với nhiều symbol
a = Symbol('Noi')
b = Symbol('Chim')
expr = 3*b + 7*a
print("Biểu thức với 'Noi' và 'Chim':", expr)  
# Truy cập tên symbol
print("Tên của a là:", a.name)
print("Tên của b là:", b.name)
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
a, b, c = symbols('a b c')
x = Symbol('x')
y = Symbol('y')
s = x*y + y**x
print("Biểu thức s = x*y + y**x:", s)
p = x*(x + 2*x)
print("Biểu thức p = x*(x + 2*x):", p)  
p = (x + 2)*(y + 3)
print("Biểu thức p = (x + 2)*(y + 3):", p)
p = (x + 2)*(y + 3) + (x + 2)*(x - 3)
print("Biểu thức đầy đủ:", p)
