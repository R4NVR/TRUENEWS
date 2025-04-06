class HDFC:
    @staticmethod
    def bank ():
        print("welcome to hdfc bank")
    def __init__ (self,name, amount,debit,credit):
        self.name=name
        self.amount=amount
        self.debit=debit
        self.credit=credit

    
    
    def newbal(self):
        
        net=self.amount-self.debit+self.credit
        print("your net balance is = ",net )
    def __password(self,password):
        self.password=PASSWORD
        


name=input("enter your name = ")
amount=int(input("enter the amount in your bank account= "))
debit=int(input("enter the amount deducted ="))
credit=int(input("enter the amount creditted to you bank"))
PASSWORD=input("enter your password= ")
b=HDFC(name,amount,debit,credit)

x=input("do you want to access your account info? enter the password= ")
if (x==PASSWORD):
    print("here is your bank information")
    b.bank()
    b.newbal()
else:
    print("wrong password")



    