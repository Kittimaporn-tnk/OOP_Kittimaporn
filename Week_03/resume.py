name = input("โปรดกรอกชื่อ\n")
height = float(input("โปรดกรอกส่วนสูง\n"))
weight = float(input("โปรดกรอกน้ำหนัก\n"))
age = input("โปรดกรอกอายุ\n")
studentid = input("โปรดกรอกรหัสประจำตัวนักศึกษา\n")
year = input("โปรดกรอกชั้นปี\n")
nickname = input("โปรดกรอกชื่อเล่น\n")
print(f"ชื่อ:  {name}  อายุ: "+str(age)+"ปี  ")
print(f"รหัสประจำตัวนักศึกษา:  {studentid}  ชั้นปี:  {year}")
print(f"ชื่อเล่น:  {nickname}")
print(f"ส่วนสูง:  {height} เซนติเมตร น้ำหนัก: {weight} กิโลกรัม")
print(f"ส่วนสูง + น้ำหนัก = {height + weight}")