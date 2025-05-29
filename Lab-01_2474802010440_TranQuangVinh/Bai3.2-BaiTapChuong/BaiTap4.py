#Bài Tập 4
print("\n1. Khai báo biến và phương trình:")
from sympy import Symbol, solve
x = Symbol('x')
y = Symbol('y')
# Định nghĩa 2 phương trình
pt1 = 2*x + 3*y - 12
pt2 = 3*x - 2*y - 5
# Giải hệ phương trình
nghiem = solve((pt1, pt2), dict=True)
print("Nghiệm của hệ phương trình:")
print(nghiem)
# Lấy nghiệm đầu tiên 
nghiem = nghiem[0]
pt1_ketqua = pt1.subs({x: nghiem[x], y: nghiem[y]})
pt2_ketqua = pt2.subs({x: nghiem[x], y: nghiem[y]})
print("Kết quả thay nghiệm vào pt1:", pt1_ketqua)
print("Kết quả thay nghiệm vào pt2:", pt2_ketqua)
