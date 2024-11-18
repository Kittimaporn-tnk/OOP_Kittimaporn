number = int(input("ป้อนสูตรคูณ: "))
for i in range(1, 25):  
    a = number * i
    if (a / 2) % 2 != 0:
     print(f"{number} x {i} = {a}") 