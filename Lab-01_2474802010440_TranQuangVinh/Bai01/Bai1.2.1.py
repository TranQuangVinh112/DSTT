#Lưu ý về các phép toán xử lý trên list 
# Khởi tạo danh sách
danhsach1 = [1., 3.]
danhsach2 = [5., 7.] 
danhsach = danhsach1 + danhsach2
print("\n1. danhsach1 + danhsach2 =", danhsach)  
danhsach_gapdoi = 2 * danhsach
print("2. 2 * danhsach =", danhsach_gapdoi)
print("3. danhsach * 2 =", danhsach * 2)
#Phép chia danh sách với số (gây lỗi)
print("4.  danhsach / 2:")
ket_qua_chia = [x/2 for x in danhsach]
print("Kết quả khi chia từng phần tử:", ket_qua_chia)

# Ghép các danh sách bằng lệnh zip:
mon_hoc = ["ToanCC", "DSTT", "ToanRR", "LaptrinhCB"]
thu_tu = [2, 3, 4, 1]
diem_so = [10, 9, 8, 7]
anh_xa = zip(thu_tu, mon_hoc, diem_so)
print("Kết quả anh_xa (dưới dạng list):")
print(list(zip(thu_tu, mon_hoc, diem_so)))
anh_xa = zip(thu_tu, mon_hoc, diem_so)
tap_hop = set(anh_xa)
print("\nKết quả tập_hop:")
print(tap_hop)
anh_xa = zip(thu_tu, mon_hoc, diem_so)
lay_TT, lay_monhoc, lay_diem = zip(*anh_xa)
print("Kết quả lay_monhoc:")
print(lay_monhoc)

#-Xây dựng danh sách:
import itertools
tap_sinh = list(itertools.chain(range(4), range(5, 10), range(15, 20)))
print("Kết quả tập_sinh:", tap_sinh)
zip_ket_qua = list(zip(range(4), range(7, 12), reversed(range(11))))
print("Kết quả zip:", zip_ket_qua)
