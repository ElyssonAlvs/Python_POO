from main import Current_account


def method1():
    print('init to method1')
    method2()
    print('init to method1')


def method2():
    print('init to method2')
    cc = Current_account('John', '123')
    try:
        for i in range(1, 15):
            cc.deposit(i + 1000)
            print(cc.balance)
            if(i == 5):
                cc = None
    except:
        print('erro')

    print('end to method2')


if __name__ == '__main__':
    print('init to main')
    method1()
    print('end to main')
