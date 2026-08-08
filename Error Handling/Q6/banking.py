accounts={"ACC-1001":5000.0,"ACC-1002":250.0,"ACC-1003":0.0}

class InsufficientFundsError(Exception):
    def __int__(self,acc_id,amnt,msg="Insufficient funds in account"):
        self.acc_id=acc_id
        self.amount=amnt
        self.message=msg
        super().__init__(f"{acc_id} {self.message}")


class InvalidAmountError(ValueError):
    def __init__(self, acc_id,amnt,msg="Invalid Amount entered"):
        self.acc_id=acc_id
        self.message=msg
        self.amount=amnt
        super().__init__(f"{acc_id} {self.message}")

def withdraw(account_id, amount):
    if account_id not in accounts:
        raise KeyError(account_id)
    if amount < 0:
        raise InvalidAmountError(account_id,amount)
    if amount > accounts[account_id]:
        raise InsufficientFundsError(account_id,amount)
    
    accounts[account_id]-=amount
    return accounts[account_id]

def processs_withdrawal(account_id,amount):
    try:
        balance =withdraw(account_id,amount)
        print(f"Withdrawal successful. New balance {balance}")
    except KeyError as ke:
        print(f"KeyError: Account {ke.args[0]} not found")
    except InvalidAmountError as ia:
        print(f"InvaldAmountError: {ia}")
    except InsufficientFundsError as ise:
        print(f"InsufficuentFundsError: {ise}")

processs_withdrawal("ACC-1001",1200)
processs_withdrawal("ACC-9999",100)
processs_withdrawal("ACC-1002",-50)
processs_withdrawal("ACC-1003",100)