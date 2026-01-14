cost = float(input("Giá cước mở cửa (VNĐ): "))

try:
    kilo = float(input("Số kilomet: "))
    
    if kilo < 0:
        print("Khoảng cách phải lớn hơn 0")
    elif kilo == 0:
        print("0 đồng vì chưa đi")
    elif kilo > 10000:  
        print("Khoảng cách quá lớn, tài xế ko chạy (<= 10000 km)")
    elif kilo > 0 and kilo <= 1:
        print(cost)
    elif 2 <= kilo <= 10:
        cost += (kilo - 1) * 13500
        print(cost)
    elif kilo >= 11:
        cost += 13500 * 9 + (kilo - 10) * 11000
        if kilo > 120:
            cost = cost * 90 / 100  
        print(cost, "VND")

except ValueError:
    print("Vui lòng nhập số hợp lệ")
