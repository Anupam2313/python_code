class email:
    def __init__(self):
        self.Email=''
        self.Passs=""
        self.menu()

    def menu(self):
        user_input=input("""
                1.create email
                2.get data
                3.reset pass
                4.exit         
                         """)
        if user_input=='1':
            self.CreateEmail_password()
        elif user_input=='2':
            self.det_data()
        elif user_input=='3':
            self.change_pin()
        else :
            exit()
    
    def CreateEmail_password(self):
        email=input("enter your email :")
        if len(email)>=6:
            if email[0].isalpha():
                if (email[-4]==".") ^ (email[-3]=="."):
                    if ("@" in email) & ('.' in email):
                        if ('gmail' in email) & ('.com' in email):
                                self.Email=email                           
                                print("your email :",email)
                        else:
                            print("please enter your valid email :")
                    else:
                        print("please enter your valid email :")
                else:
                    print("please enter your valid email :")
            else:
                print("please enter your valid email :")
        else:
            self.CreateEmail_password()
        
        password=input("enter your password")
        if len(password)>=5:
            if password[0]:
                if ("@" in password) ^("#" in password) ^ ("$" in password):
                    if password[0].upper():
                        self.Passs=password
                        print("your passs",password)
                    else:
                        print("please use uper case :")
                else:
                    print("please use spcile chareter :")
            else:
                print("please enter digit number :")
        else:
            print("please enter minmum 8 digit password :")
        self.menu()

    def det_data(self):
        myemail=input("enter your email :")
        mypass=input("enter your password :")
        if self.Email==myemail:
            if self.Passs==mypass:
                print("""
                   hii this is anupam my name is anumapm tiwari 
                      i am from india ,utter pardaes ,ayodhya 
                      curently i am MCA finl year student
                      thank you
                      """)
            else:
              print("please enter yoyr valide password :")
        else:
            print("please enter yoyr valide email :")
        
        self.menu()

    def change_pin(self):
        user_password=input("enter your password :")
        if self.Passs==user_password:
            new_password=input("enter your new password :")
            self.Passs=new_password
        else:
            print("please enter your password :")
        self.menu()


w_email=email()
print(w_email)
