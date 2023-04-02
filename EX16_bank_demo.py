from bank_ac import Account

James = Account(20)
James.deposit(5)
James.withdraw(10)
James.add_interest(1.02)
print()

Robert = Account(0)
Robert.deposit(10)



print()
print(Account.get_total_balance())
