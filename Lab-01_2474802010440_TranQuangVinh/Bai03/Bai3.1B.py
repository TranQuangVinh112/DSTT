# Lưu ý - Trong numpy:
import numpy as np
# vec3 để thử truy xuất phần tử
vec3 = np.array([2., 4., 6.])
print("vec3 =", vec3)
print("vec3[2] =", vec3[2])  # Truy xuất phần tử thứ 3 (chỉ số 2)
# Tạo vector bằng linspace
vec4 = np.linspace(0, 20, 5)
print("\nvec4 (linspace 0 -> 20 với 5 phần tử) =", vec4)
# Vector toàn 0
vec5 = np.zeros(5)
print("\nvec5 (toàn 0) =", vec5)
# Vector toàn 1
vec6 = np.ones(5)
print("vec6 (toàn 1) =", vec6)
# Vector ảo (giá trị rác trong bộ nhớ)
vec7 = np.empty(5)
print("vec7 (empty - giá trị không xác định) =", vec7)
# Vector ngẫu nhiên từ 0 đến 1
try:
    rand_vec = np.rand(5)  # Dòng này sẽ bị lỗi vì np.rand không tồn tại
except AttributeError:
    rand_vec = np.random.random(5)  # Cách đúng
print("\nVector ngẫu nhiên từ 0 đến 1:", rand_vec)
