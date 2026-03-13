a, b= map(int, input("Nhập 2 cạnh: ").split())
if a>b:
    c=b*b*3.14/4
    dientich=a*b-c
    print("Diện tích còn để trồng cây xung quanh là: " , round(dientich, 2))
else:
    c=a*a*3.14/4
    dientich=a*b-c
    print("Diện tích còn để trồng cây xung quanh là: " , round(dientich, 2))
