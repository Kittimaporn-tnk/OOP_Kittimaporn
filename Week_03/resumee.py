name = input("โปรดกรอกชื่อ\n")
age = input("โปรดกรอกอายุ\n")
stuid = input("โปรดกรอกรหัสประจำตัวนักศึกษา\n")
year = input("โปรดกรอกชั้นปี\n")
nickname = input("โปรดกรอกชื่อเล่น\n")
height = float(input("โปรดกรอกส่วนสูง\n"))
weight = float(input("โปรดกรอกน้ำหนัก\n"))
hw = height + weight
print("ชื่อ:" + name + "อายุ:" + age)
print("รหัสประจำตัวนักศึกษา:" + stuid + "ชั้นปี:" + year)
print("ชื่อเล่น:" + nickname)
print("ส่วนสูง:" + str(height) + "น้ำหนัก:" + str(weight))
print("ส่วนสูง + น้ำหนัก" + str(hw))