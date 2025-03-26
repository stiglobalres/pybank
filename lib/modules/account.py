from lib.types.accountInfo import accountInfoType

class Account:
    def __init__(self,  person=[]) -> None:
        self._accno = ''
        self.__accounts = person
   
    def getAccountInfo(self, accno: int):
        print(f"{self.__accounts}")
        account = [i for i in self.__accounts if i[accountInfoType.ACCOUNT_NUMBER]==accno]
        return account[0] if len(account) else {}

    def _creatAccount(self, firstname: str, lastname: str):
        id = int(len(self.__accounts) + 1000)
        account = {
            accountInfoType.ACCOUNT_NUMBER: id,
            accountInfoType.FIRST_NAME: firstname,
            accountInfoType.LAST_NAME: lastname
        }
        self.__accounts.append(account)
        
        return account
