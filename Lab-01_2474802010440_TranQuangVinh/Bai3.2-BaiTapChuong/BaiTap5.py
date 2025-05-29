#Bài Tập 5
import numpy as np
M1 = np.array([[9, 12], [23, 30]])
print("Ma trận M1:\n", M1)
u = np.array([2, 1])
print("Vector u:\n", u)
tichM1u = M1.dot(u)
print("M1.dot(u):", tichM1u)
tichuM1 = u.dot(M1)
print("u.dot(M1):", tichuM1)
print("np.dot(M1, u):", np.dot(M1, u))
print("np.dot(u, M1):", np.dot(u, M1))

#-Sinh viên thực hành và cho biết kết quả các lệnh sau:
# mat1 là ma trận 5x5 toàn số 0
mat1 = np.zeros([5,5])
print("mat1 = zeros(5,5):\n", mat1)  # Cho biết mat1?
mat2 = np.ones([5,5])
print("\nmat2 = ones(5,5):\n", mat2)  # Cho biết mat2?
mat3 = mat1 + 2*mat2
print("\nmat3 = mat1 + 2*mat2:\n", mat3)  # Cho biết mat3?
mat4 = mat3
mat3[3][2] = 10
print("\nSau khi mat3[3][2] = 10:")
print("mat3:\n", mat3)
print("mat4:\n", mat4)  # mat3 thay đổi thì mat4 có thay đổi theo không?
mat5 = np.copy(mat3)
mat3[3][2] = 20
print("\nSau khi mat3[3][2] = 20:")
print("mat3:\n", mat3)
print("mat4:\n", mat4)  # mat3 thay đổi thì mat4 có thay đổi theo không?
print("mat5:\n", mat5)  # mat3 thay đổi thì mat5 có thay đổi theo không?
mat6 = np.empty([4,5])
print("\nmat6 = empty(4,5):\n", mat6)  # Hãy cho biết mat6?
mat7 = np.identity(4)
print("\nmat7 = identity(4):\n", mat7)  # Hãy cho biết mat7?
try:
    mat8 = np.rand(4,5)
except AttributeError:
    mat8 = np.random.random([4,5])
print("\nmat8 = random(4,5):\n", mat8)  # Hãy cho biết mat8?

