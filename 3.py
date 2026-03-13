a=input("Nhập 1 kí tự ")
if a.isupper():
    print(a.lower())
elif a.islower():
    print(a.upper())
else :
    print("Kí tự vừa nhập không phải chữ")