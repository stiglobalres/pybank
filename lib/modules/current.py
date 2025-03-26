class Currents:
    def __init__(self, accno: int) -> None:
        self._accno = accno
        self.__savings = {}
        
    def _createAccount(self)->None:
        self.__savings[self._accno] = 0

    def _deposit(self, amount:float):
        bal = self.__savings[self._accno]
        self.__savings[self._accno] =bal + amount
        return

    def _withdrawal(self, amount: float):
        bal = self.__savings[self._accno]
        self.__savings[self._accno] = bal - amount
        return

    def _balance(self)->float:
        return float(self.__savings[self._accno])
