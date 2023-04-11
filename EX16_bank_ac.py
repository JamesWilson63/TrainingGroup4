class InsufficientFundsException(Exception):

    def __init__(self, amt):
        self.msg = f'You do not have enough funds to withdraw {amt}'

    def __str__(self):
        return self.msg



class Account:
    ac_num = 10000000
    totalDeposits = 0
    intrest_rate = 1.02

    def __init__(self, initial):
        self._balance = initial
        Account.ac_num += 1
        print("Account number: ", Account.ac_num)
        print("You have opened a new account with a Balance of :£", self._balance)

    def deposit(self, amt):
        self._balance += amt
        Account.totalDeposits += amt
        print("You have made a deposit of :£", amt, "Your new balance is :£", self._balance)

    def withdraw(self,amt):
        if amt > self._balance:
            raise InsufficientFundsException(amt)
        else:
            self._balance -= amt
            Account.totalDeposits -= amt
            print("You have withdrawn :£", amt, "Your new balance is :£", self._balance)

    def getbalance(self):
        return self._balance

    def add_interest(self, int):
        self._balance *= int
        Account.totalDeposits *= int
        print("you received an interest payment of :", (int*100-100),"%","", "Your new balance is :£", self._balance)


    def __gt__(self, other):
       return self._balance > other.getbalance()

    def __lt__(self, other):
       return self._balance < other.getbalance()

    @classmethod
    def get_total_balance(cls):
        return f"The Royal Bank of James has assets of :  £{cls.totalDeposits}"