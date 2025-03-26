from lib.types.input import InputType
from lib.types.bankAccounts import bankAccountType
from lib.types.accountInfo import accountInfoType
from lib.modules.account import Account
from lib.modules.savings import Savings
from lib.modules.current import Currents
from lib.types.savingMenuType import savingMenuType
from lib.components.menu import Menu
from lib.components.clearScreen import ClearScreen
from lib.components.form import Form

class Bank:
    CREATE_ACCOUNT = 1
    OPEN_ACCOUNT = 2

    def __init__(self):
        self._mainOption=None
        self._accno=None
        self._account = {}
        self._firstname = None
        self._lastname = None
        self._continue = True
        self.main()

    def main(self):
        while self._continue:
            ClearScreen._clear_screen(self._account)
            if(self._mainOption == self.CREATE_ACCOUNT):
                if self._firstname == None:
                    self._firstname = Form._input_form("Enter your first name:", InputType.ALPHA , 2 )

                if self._lastname == None:
                    self._lastname = Form._input_form("Enter your last name:", InputType.ALPHA , 2)
                
                ClearScreen._clear_screen(self._account)

                opt = Form._input_form("Would you like to create a new account under this name?", InputType.NUMBER, 1,{1:"YES",2:"NO"})
                if opt == 1:
                    account = Account()
                    accountInfo = account._creatAccount(self._firstname, self._lastname)
                   
                    if len(accountInfo):
                        self._accno = int(accountInfo[accountInfoType.ACCOUNT_NUMBER])
                        self._account = accountInfo

                        savings = Savings(self._accno)
                        savings._createAccount()
                        
                        current = Currents(self._accno)
                        current._createAccount()

                        self._mainOption=2
                        
                        self.__bank_transaction()

                else:
                    self._mainOption = self.main_menu()

            elif(self._mainOption == self.OPEN_ACCOUNT):
                self.__open_account()
            else:
                self._mainOption = self.main_menu()
        
    def main_menu(self)->int:
        ClearScreen._clear_screen(self._account)
        self._mainOption= self._firstname = self._lastname = self._accno = None
        self._account = {}
        options = {
            self.CREATE_ACCOUNT : "Create Account",
            self.OPEN_ACCOUNT : "Enter Account"
        }
        return Form._input_form("Choose type of transaction:", InputType.NUMBER, 1 ,options)

    def __transaction_savings(self, savings:Savings)->None:
        while True:
            res1 = Menu._savings_menu()
            if res1 == savingMenuType.DEPOSIT:
                ## TODO ##
                ClearScreen._clear_screen(self._account)
                amount = Form._input_form("Enter the amount:", InputType.CURRENCY)
                savings._deposit(amount)

                ClearScreen._clear_screen(self._account)
                bal = f"  Your Remaing Balance: {savings._balance(): .2f}  " 
                print(f"{bal.center(50,'*')} \n")

            elif res1 == savingMenuType.WITHDRAWAL:
                ### TODO ###
                ClearScreen._clear_screen(self._account)
                amount = Form._input_form("Enter the amount:", InputType.CURRENCY)
                savings._withdrawal(amount)

                self._show_savings_balance(savings)

            elif res1 == savingMenuType.BALANCE:
                self._show_savings_balance(savings)
            else:
                break

    def __transaction_current(self):
         ### TODO ###
        pass

    def __open_account(self):
        ctr = 0
        openAccountFlag = True
       
        if self._accno ==None:
            while openAccountFlag:
                accno = Form._input_form("Enter You Account Number:", InputType.NUMBER, 4)
                
                ClearScreen._clear_screen(self._account)
                person = Account()
                self._account = person.getAccountInfo(int(accno))
                if len(self._account):
                    self._accno = int(accno)
                    openAccountFlag= False
                else:
                    ctr +=1
                    print('Try Again')
                    
                if(ctr >= 3):
                    # Exit after 3 tries
                    self._mainOption=None
                    openAccountFlag = False
                
                
        else:
            self.__bank_transaction()

    def __bank_transaction(self):

        savings = Savings(self._accno)
        current = Currents(self._accno)
        ClearScreen._clear_screen(self._account)

        opt = Menu._account_menu()
        if opt == bankAccountType.SAVING:
            ClearScreen._clear_screen(self._account)
            self.__transaction_savings(savings)
        elif opt == bankAccountType.CURRENT:
            self.__transaction_current()
        else:
            #Exit to main screen
            self._mainOption = self.main_menu() 
  
    def _show_savings_balance(self, Savings: Savings):
        ClearScreen._clear_screen(self._account)
        bal = f"  Your Remaing Balance: {Savings._balance(): .2f}  " 
        print(f"{bal.center(50,'*')} \n")
        pass

bank = Bank()

