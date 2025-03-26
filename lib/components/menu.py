from lib.types.bankAccounts import bankAccountType
from lib.types.input import InputType
from lib.components.form import Form
from lib.types.savingMenuType import savingMenuType

class Menu:
    def _account_menu()->int:
        options = {
            bankAccountType.SAVING: bankAccountType.SAVING_LABEL,
            bankAccountType.CURRENT: bankAccountType.CURRENT_LABEL,
            bankAccountType.BACK: bankAccountType.BACK_LABEL   
        }
        res = Form._input_form("Choose account type", InputType.NUMBER, 1 , options)
        return int(res)

    def _savings_menu()->int:
        options = {
            savingMenuType.DEPOSIT: savingMenuType.DEPOSIT_LABEL,
            savingMenuType.WITHDRAWAL: savingMenuType.WITHDRAWAL_LABEL,
            savingMenuType.BALANCE: savingMenuType.BALANCE_LABEL,
            savingMenuType.BACK: savingMenuType.BACK_LABEL
        }
        return Form._input_form("Choose Transaction type", InputType.NUMBER, 1 , options)
