class BanAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
        self.is_active=True
        
    def depositar(self,amount):
        if self.is_active:
            self.balance += amount
            print(f'Se ha depositado {amount}. Saldo actual {self.balance}')
        else:
            print('No se puede depositar, cuenta inactiva')
            
    def retirar(self, amount):
        if self.is_active:
            if amount <=self.balance:
                self.balance -= amount
                print(f'Se ha retirado {amount}. Saldo actual {self.balance}')   
    
    def deactivate_account(self):
        self.is_active=False
        print(f'La cuenta ha sido desactivada')
        
    def activate_account(self):
        self.is_active=True
        print(f'La cuenta ha sido activada')
        
account1=BanAccount('Ana',500)
account2=BanAccount('Luis',1000)

account1.depositar(200)
account2.depositar(100)
account1.deactivate_account()
account1.depositar(50)
account1.activate_account()
account1.depositar(50)

        
                   