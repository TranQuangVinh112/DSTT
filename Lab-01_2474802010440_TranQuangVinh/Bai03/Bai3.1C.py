# - Các lệnh xử lý
import numpy as np
# Khởi tạo vector v
v = np.array([1., 3., 5.])
print("v =", v)
# Tổng các phần tử
print("\nTổng các phần tử của v:", np.sum(v))
# Số chiều
print("Số chiều (shape) của v:", v.shape)
# Chuyển vị vector
print("Chuyển vị của v:", v.transpose())  # với vector 1 chiều, kết quả không đổi
# Cắt lấy phần đầu của vector
v1 = v[:2]
print("\nv1 = v[:2] =", v1)
# Gán phần tử đầu của v
v[0] = 5
print("v sau khi v[0] = 5:", v)
print("v1 sau khi thay đổi v:", v1)  # v1 thay đổi do cùng tham chiếu
# Gán giá trị mới cho v1[:2]
try:
    v1[:2] = [1., 2., 3.]  # Sai: quá số phần tử
except ValueError as e:
    print("Gán v1[:2] = [1., 2., 3.]:", e)
v1[:2] = [1., 2]
print("\nv1 sau khi gán [1., 2]:", v1)
print("v sau khi gán v1:", v)
# Tạo v3 từ phép toán với v và v1
v3 = 2 * v[:2] + v1 * 3
print("\nv3 = 2*v[:2] + 3*v1 =", v3)
# Gán lại v1 bằng list mới, v3 không thay đổi vì đã tính xong trước đó
v1 = np.array([4, 6])
print("v1 mới =", v1)
print("v3 sau khi thay đổi v1:", v3)
print("v hiện tại:", v)
# Một số phép toán khác
print("\nv + 10.0 =", v + 10.0)
print("Căn bậc 2 của v:", np.sqrt(v))
print("Cos(v):", np.cos(v))
print("Sin(v):", np.sin(v))
# Tích vô hướng (dot product)
print("\nv1 =", v1)
print("v3 =", v3)
print("np.dot(v1, v3) =", np.dot(v1, v3))
print("v1.dot(v3) =", v1.dot(v3))
print("v3.dot(v1) =", v3.dot(v1))
