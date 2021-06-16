class Account:
    
    def __init__(self,owner,balance = 0):
        
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        
        return 'Account Owner: {}\nAccount Balance: ${}' .format(self.owner,self.balance)
    
    def Deposit(self, amt):
        
        if(amt <0):
            print("Cannot make a negative withdrawal!")
        else:
            self.balance += amt
            print('Deposit accepted!')
            print('Available Balance: $' + str(self.balance))
            
    def withdraw(self,amt):
        
        if(amt > self.balance):
            print('GET THE FUCK OUTTA HERE!')
        elif(amt < 0):
            print('Cannot make a negative withdraw... That would be a deposit!')
        else:
            print('Here is $' + str(amt))
            self.balance -= amt
            print('Available balance: $' + str(self.balance))
            
acct = Account('Jackson',100)
print(acct)
acct.withdraw(27.5)
acct.Deposit(32.18)
acct.withdraw(1000)
acct.withdraw(-23)