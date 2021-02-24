def deposit(balance, money):
    print("입금이 완료되었습니다. \n잔액은 {0}원입니다." .format(balance+money))
    return balance+money

balance=0 
balance = deposit(balance, 1000)

def withdraw(balance, money):
    if balance >= money :
        print("출금이 완료되었습니다.\n잔액은 {0}원입니다.".format(balance-money))
        return balance-money
    else:
        print("잔액이 부족합니다.\n잔액은 {0}원입니다." .format(balance))
        return balance

balance = 0 
balance = deposit(balance,1000)
balance = withdraw(balance,500)

def withdraw_night(balance, money):
    commision = 100 # 수수료
    return commision, balance-money-commision

commision,balance=withdraw_night(2000,1000)

print("수수료는 {0}원, 잔액은 {1}원입니다." .format(commision, balance))