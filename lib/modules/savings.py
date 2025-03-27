class Savings:
    STATUS = 'status'
    MESSAGE = 'msg'
    RESPONSE = 'response'

    def __init__(self, accno: int, savings={}) -> None:
        self._accno = int(accno)
        self._savings = savings
        
    def _createAccount(self):
        try:
            self._savings[self._accno] = 0
            return {
                self.STATUS:True, 
                self.RESPONSE:'Successfully created a savings account.'
            }  
        except ValueError:
            return {
                self.STATUS:False, 
                self.MESSAGE:'Unable to create savings account.'
            }               

    def _deposit(self, amount:float):
        bal = self._savings[self._accno]
        deposit = float(amount)
        if deposit > 0:
            self._savings[self._accno] =bal + float(amount)
            return {
                self.STATUS:True, 
                self.RESPONSE:'Amount was successfully added to your savings'
            }
        else:
            return {
                self.STATUS:False, 
                self.MESSAGE:'Invalid amount'
            }

    def _withdrawal(self, amount: float):
        bal = float(self._savings[self._accno])
        if bal >= float(amount):
            self._savings[self._accno] = bal - amount
            return {
                self.STATUS:True, 
                self.RESPONSE:'Amount was successfully deducted from your savings'
            }
        else:
            return {
                self.STATUS:False, 
                self.MESSAGE:'Not enough funds'
            }

    def _balance(self):
        if self._accno in self._savings:
            return {
                self.STATUS: True, 
                self.RESPONSE: float(self._savings[self._accno])
            }  
        else:
            return {
                self.STATUS:False, 
                self.MESSAGE:'No Saving Account Available'
            }          

