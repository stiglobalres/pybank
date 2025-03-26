import os

class ClearScreen:

    def _clear_screen( account)->None:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if len(account):
            name = "Welcome {} {} ".format(account['firstname'], account['lastname'])
            accno = f"Account Number: {account['id']}"
            print("#" * 50)
            print(f"##{name.center(46)}##")
            print(f"##{accno.center(46)}##")
            print("#" * 50)
            print("\n")    