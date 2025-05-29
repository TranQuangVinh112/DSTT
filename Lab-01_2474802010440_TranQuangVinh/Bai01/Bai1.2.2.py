#1
print("\n1. Thao tác với list:")
try:
    mylin = [10, 20, 30]
    print("mylin =", mylin)
    a = b = c = 0
    print("a, b, c =", a, b, c) 
    mylin_empty = []
    print("mylin_empty =", mylin_empty) 
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#2
print("\n2. Import module:")
try:
    print("Giả định import từ file fluctial1.py")
    print("Đã import module (giả định)")
except ImportError:
    print("Không tìm thấy file module!")
except Exception as e:
    print("Lỗi khác:", e)