try:  
    num = int(input("ป้อนค่า : "))  
    if num == 0:
        raise ZeroDivisionError()
    elif num < 0 :
        raise Exception()
    elif num >= 5000:
        r =  num * 0.2
        r1 = num - r
        print(f"20% Discount = {r} num = {r1}")
    elif num >= 2000:
        r =  num * 0.1
        r1 = num - r
        print(f"10% Discount = {r} num = {r1}")
    else:
        print("คุณไม่ได้รับส่วนลด")
except ValueError:
    print("ใส่เฉพาะตัวเลข")
except ZeroDivisionError:
    print("ห้ามใส่ 0")
except:
    print("ห้ามใส่ค่าติดลบ")