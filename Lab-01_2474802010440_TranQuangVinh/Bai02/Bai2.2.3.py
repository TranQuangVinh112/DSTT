# Thay thế giá trị 
from sympy import Symbol, simplify, sin, cos
x = Symbol('x')
y = Symbol('y')
# Định nghĩa biểu thức
bieuthuc = x*x - x*y + y*y
print("Biểu thức ban đầu:")
print(bieuthuc)  # x**2 - x*y + y**2
# Thay thế giá trị x=3, y=2
giatri = bieuthuc.subs({x:3, y:2})
print("\nThay x=3, y=2:")
print(giatri)  # 7
# Kiểm tra biến x, y không đổi
print("\nBiến x, y sau khi subs():")
print("x =", x)  # x
print("y =", y)  # y
#1: x=3, y=x
giatri_tinhhuong1 = bieuthuc.subs({x:3, y:x})
print("\nTình huống 1: x=3, y=x:")
print(giatri_tinhhuong1)  # 9 - 3*x + x**2
#2: x=y, y=3
giatri_tinhhuong2 = bieuthuc.subs({x:y, y:3})
print("\nTình huống 2: x=y, y=3:")
print(giatri_tinhhuong2)  # y**2 - 3*y + 9
#3: y=x rồi x=3
giatri_tinhhuong3 = bieuthuc.subs({y:x}).subs({x:3})
print("\nTình huống 3: y=x rồi x=3:")
print(giatri_tinhhuong3)  
# Thay x bằng (1 - y)
bieuthuc_moi = bieuthuc.subs({x:1 - y})
print("\nBiểu thức sau khi thay x = 1 - y:")
print(bieuthuc_moi) 
# Rút gọn biểu thức mới
dongian = simplify(bieuthuc_moi)
print("\nBiểu thức sau khi simplify:")
print(dongian)  
# Ví dụ lượng giác
bt = sin(x)*cos(y) + cos(x)*sin(y)
bt_moi = simplify(bt)
print("\nBiểu thức lượng giác ban đầu:")
print(bt)  
print("\nBiểu thức lượng giác sau simplify:")
print(bt_moi)  
