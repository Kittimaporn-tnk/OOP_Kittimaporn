number = int(input("ป้อนสูตรคูณ: "))
i = 1  
while i < 25:  
    a = number * i
    if (a / 2) % 2 != 0:
        print(f"{number} x {i} = {a}") 
    i += 1   