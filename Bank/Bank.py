# ELYBANK 😀 with procedural language
def create_account(number, holder, balance, limit):
    account = {'Number': number, 'Holder': holder,
               'Balance': balance, 'Limit': limit}
    return account


def deposit_money(account, value):
    account['Balance'] += value


def withdraw_money(account, value):
    account['Balance'] -= value


def extract_account(account):
    print('Number : {}\nBalance : {}'.format(
        account['Number'], account['Balance']))


account = create_account('123-4', 'João', 120.0, 1000.0)
deposit_money(account, 15.0)
extract_account(account)

# Number: '123-4'
# Saldo: '135.0'

withdraw_money(account, 20.0)
extract_account(account)

# Number : '123-4'
# Balance : 115.0
