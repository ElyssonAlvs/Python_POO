from classes import Historic, Client, Account, Account_updater, Current_account, Savings_account, TaxableMixIn, Life_insurance
# -------------------------------------------------------
# Tests 1
"""
client = Client('João', 'Oliveira', '1111111111-1')
my_account = Account('123-4', client, 120.0, 1000.0)

account = Account('123-4',	'João',	120.0,	1000.0)
account.deposit_money(20.0)
account.extract_account

# number : '123-4'
# balance : 140.0

account.withdraw_money(15)
account.extract_account()

print(account.number)
print(account.holder)
print(account.balance)
print(account.limit)
"""
# ------------------------------------------------------------------
# Tests 2
"""
client1 = Client('João', 'Oliveira', '11111111111-11')
client2 = Client('José', 'Azevedo',	'222222222-22')
account1 = Account('123-4', client1, 1000.0)
account2 = Account('123-5', client2, 1000.0)
account1.deposit_money(100.0)
account1.withdraw_money(50.0)
account1.transfer_money(account2, 200.0)
account1.extract_account()

# numero : 123-4
# saldo : 850.0

account1.historic.prints()

# Open date:	2018-05-10	19:44:07.406533
# transactionss:
# - deposit	of 100.0
# - Withdrawal of 50.0
# - Withdrawal of 200.0
# - Transfer of 200.0 from account 123-5
# - Took extract - balance of 850.0

account2.historic.prints()

# Open date:	local date of compiuter
# Transactions:
# - Withdrawal of 200.0
"""
# Test 3
if __name__ == '__main__':
    c = Account('123-4', 'John', 1000.0)
    cc = Current_account('123-5', 'Jose', 1000.0)
    cp = Savings_account('123-6', 'Maria', 1000.0)
    
    adc = Savings_account(0.01)

    adc.run(c)
    adc.run(cc)
    adc.run(cp)

    print(f'Total Balance: {adc.total_balance}')
"""
    c.actualize(0.01)
    cc.actualize(0.01)
    cp.actualize(0.01)
    
    print(c.balance)
    print(cc.balance)
    print(cp.balance)
    print(cc)
"""
