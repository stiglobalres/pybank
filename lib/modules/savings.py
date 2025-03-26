class Savings:
    def __init__(self, accno: int, savings={}) -> None:
        self._accno = int(accno)
        self._savings = savings
        
    def _createAccount(self)->bool:
        self._savings[self._accno] = 0

    def _deposit(self, amount:float):
        bal = self._savings[self._accno]
        self._savings[self._accno] =bal + amount
        return

    def _withdrawal(self, amount: float):
        bal = self._savings[self._accno]
        self._savings[self._accno] = bal - amount
        return

    def _balance(self)->float:
        #print(f" Accessing Saving Accoung for {self._accno} ")
        #print(f" Accessing Saving Accoung for: {self._savings} ")
        return float(self._savings[self._accno])

