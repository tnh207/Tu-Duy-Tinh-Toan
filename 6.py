a, b, c = map(float, input("Nhập 3 cạnh của tam giác : ").split())
import math
if a+b>c and a+c>b and b+c>a :
    ncv=(a+b+c)/2
    dt=(ncv-a)*(ncv-b)*(ncv-c)*(ncv)
    print("Diện tích của tam giác là : ",  round(math.sqrt(dt), 1))
else:
    print("Không phải là tam giác")