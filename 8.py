tenchuho = input("Nhập tên chủ hộ = ")
a = int(input("Chỉ số tháng trước : "))
b = int(input("Chỉ số tháng sau : "))

c = b - a

print("Tên chủ hộ :", tenchuho)

if c <= 50:
    c = c * 1984
    print("Tiền phải trả là", c)

elif c <= 100:
    c = c * 2050
    print("Tiền phải trả là", c)

elif c <= 200:
    c = c * 2380
    print("Tiền phải trả là", c)

elif c <= 300:
    c = c * 2998
    print("Tiền phải trả là", c)

elif c <= 400:
    c = c * 3350
    print("Tiền phải trả là", c)

else:
    c = c * 3460
    print("Tiền phải trả là", c)