class Bank :
    def __init__(self,id,name,balance):
        self.id = id
        self.name = name
        self.__balance = balance
    def deposit(self,amount):
        if amount >= 100 :
            self.__balance += amount
        else:
            print('ใส่ยอดเงิน 100 บาทขึ้นไป')
    def withdraw(self,amount):
        if amount > 0 and amount <= self.__balance :
            self.__balance -= amount
        else :
            print('ยอดเงินไม่ถูกต้อง')
    def check(self):
        print(self.__balance)
    def check (self) :
        return self.__balance
id1 = Bank(1,"rose",5000)
id1.__balance += 5000
id1.deposit(300)
print(f'เงินของ {id1.name} มีอยู่ {id1.check()} บาท')