from EX16_bank_ac import Account, InsufficientFundsException

#James = Account(20)
#James.deposit(5)
#James.withdraw(10)
#James.add_interest(1.02)
#print()

Robert = Account(0)
Robert.deposit(10)
Robert.deposit(11)
try:
    Robert.withdraw(22)
except InsufficientFundsException as e:
    print(e)



print()
print(Account.get_total_balance())
