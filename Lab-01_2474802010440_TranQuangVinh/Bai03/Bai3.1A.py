#-Một số lệnh cơ bản numpy xử lý vector
import numpy as np
# Định nghĩa vec1
vec1 = np.array([1., 3., 5.])
print("vec1 =", vec1)
# vec1 * 2
print("\nvec1 * 2 =", vec1 * 2)
# vec1 * vec1 (element-wise multiplication)
print("vec1 * vec1 =", vec1 * vec1, "# Đây là phép nhân từng phần tử")
# vec1 / 2
print("vec1 / 2 =", vec1 / 2)
# vec1 + vec1
print("vec1 + vec1 =", vec1 + vec1)
# vec2 có kích thước khác vec1
vec2 = np.array([2., 4.])
try:
    result = vec1 + vec2
    print("vec1 + vec2 =", result)
except ValueError as e:
    print("vec1 + vec2: Lỗi -", e)
    print("lỗi,Lý do: vec1 có 3 phần tử, vec2 chỉ có 2 phần tử → không thể cộng.")
# vec3 có cùng kích thước với vec1
vec3 = np.array([2., 4., 6.])
print("\nvec3 =", vec3)
print("vec1 + vec3 =", vec1 + vec3)
print("vec1 / vec3 =", vec1 / vec3)
print("vec1 * vec3 =", vec1 * vec3)
print("2 * vec1 + 5 * vec3 =", 2 * vec1 + 5 * vec3)
