number = list(map(int, input("Nhập các số phân biệt nhau bằng dấu cách : ").split()))
a = 0

for i in number:
    if i % 2 != 0:
      a=a+ 1

print(a)