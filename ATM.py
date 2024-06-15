class ATM:
    def __init__(self):
        self.pin=''
        self.balance=0
        self.menu()
    def menu(self):
        user=input("""
                    1.create pin1
                    2.check balance
                    3.change pin
                    4.to withdrow
                    5.exit
                    """)
        if user=="1":
            self.create_pin()
        elif user=="2":
            self.check_balance()
        elif user=="3":
            self.change_pin()
        elif user=="4":
            self.withdrow_b()
        else:
            exit()
    def create_pin(self):
        user_pin=input("enter your password :=>")
        self.pin=user_pin

        user_balance=int(input("enter b."))
        self.balance=user_balance
        print("pin created sucesful")
        self.menu()
    def check_balance(self):
        user_pin=input("enter your pin :=>")
        if self.pin==user_pin:
            print("your balance",self.balance)
        else:
            print("please enter your currect pin :")
        self.menu()
    def change_pin(self):
        user_pin=input("please enter your pin :=>")
        if self.pin==user_pin:
            new_pin=input("enter your new pin :=>")
            self.pin=new_pin
        else:
            print("sorry")
        self.menu()
    def withdrow_b(self):
        user_pin=input("enter yor pin :")
        if user_pin==self.pin:
            user_balance=int(input("enter your balance :=>"))
            if self.balance>=user_balance:
                self.balance=self.balance-user_balance
                print("your new balance :",self.balance)
            else:
                print("limit crouss")
        else:
            print("enter your currect pin")
        self.menu()
obj=ATM()
print(obj)
