
class customer :
    def __init__(self,customer_name,customer_surname,customer_TR_ID_number,customer_phone_number):
        self.name = customer_name
        self.surname = customer_surname
        self.tc_identification = customer_TR_ID_number
        self.phone = customer_phone_number
    def display_information(self):
        print (f'Customer Information:\nName: {self.name}\nSurname: {self.surname}')
        print(f'customer TR ID number:{self.tc_identification},\ncustomer phone numbe:{self.phone}')


class account:
    def __init__(self,Customer_object,account_number,account_balance = 0):
        # super().__init__(customer.name,customer.surname,customer.tc_identification,customer.phone)
        self.customer = Customer_object
        self.account_number = account_number
        self.balance = account_balance
    def deposit(self, amount):
        if amount > 0 :
            self.balance += amount
            print (f'Depset amount = {amount} €\nNew balnce + {self.balance} € ')
        else:
            print( "You enterd a wrong amount" )

    def money_check(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'Withdraw amount : {amount}€ , New Balance:{self.balance}€')
        else:
            print(f"Insufficiant balance you can not withdraw because your current balance is {self.balance}€ is less than the withdraw amount {amount} ")
    def dicplay_balance(self):
        print(f'Your Balance is: {self.balance}€')

customer_num_1  = customer("Mohamed", "Azaam", "98574395", "0654289825")
account1 = account(customer_num_1, "NL6589244425", 700)

# Display customer information
customer_num_1.display_information()
account1.dicplay_balance()
account1.deposit(300)
account1.money_check(800)  # Should succeed
account1.money_check(300)  # Should fail due to insufficient balance
account1.dicplay_balance()