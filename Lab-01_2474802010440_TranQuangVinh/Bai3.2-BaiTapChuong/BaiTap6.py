import numpy as np
# Khai báo các ma trận nguy cơ (4x5)
A = np.array([
    [0, 1, 1, 3, 1],
    [0, 0, 1, 0, 1],
    [1, 5, 2, 2, 0],
    [0, 1, 2, 1, 2]
])
B = np.array([
    [1, 1, 2, 2, 2],
    [1, 2, 0, 0, 1],
    [1, 4, 2, 1, 2],
    [2, 2, 0, 1, 2]
])
C = np.array([
    [0, 5, 0, 1, 1],
    [1, 1, 1, 1, 3],
    [1, 3, 0, 1, 3],
    [1, 3, 3, 0, 2]
])
D = np.array([
    [3, 1, 5, 0, 1],
    [0, 3, 7, 7, 0],
    [5, 0, 0, 3, 5],
    [3, 2, 0, 0, 0]
])
E = np.array([
    [1, 0, 0, 0, 0],
    [10, 0, 15, 0, 0],
    [0, 5, 0, 15, 5],
    [0, 0, 2, 0, 0]
])
# Hàm kiểm tra vùng an toàn: tổng nguy cơ <= 5
def an_toan(total_risk):
    return total_risk <= 5
# a. 
risk_a = E
safe_a = an_toan(risk_a)
print("a. An toàn chiến dịch ngắn hạn:\n", safe_a.astype(int), "\n")
# b. 
risk_b = A + B + C  # A: cháy rừng, B: lũ quét, C: sạt lở núi
safe_b = an_toan(risk_b)
print("b. An toàn tập luyện thời bình:\n", safe_b.astype(int), "\n")
# c.
risk_c = A + D
safe_c = an_toan(risk_c)
print("c. An toàn theo mùa khô:\n", safe_c.astype(int), "\n")
# d.  
risk_d = B + C + D
safe_d = an_toan(risk_d)
print("d. An toàn mùa mưa:\n", safe_d.astype(int), "\n")
# e. 
risk_e = A + B + C + D + E
safe_e = an_toan(risk_e)
print("e. An toàn trong 8 tháng:\n", safe_e.astype(int), "\n")
