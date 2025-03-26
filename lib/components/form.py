from lib.components.clearScreen import ClearScreen
from lib.types.input import InputType
class Form:

    def _input_form(text: str, inputType: int, minLen:int = 1, options={} ):
        cb_val = None

        while True:
            print(text)
            if len(options):
                for k,v in options.items():
                    print(f"{k}: {v}")
            val = input('>> ')

            if(inputType == InputType.ALPHA):
                if val.isalpha() and len(val) >= minLen:
                    cb_val = val.capitalize()
                    break
                else:
                    print("INVALID: Only alphabetic letters are allowed.")

            elif inputType == InputType.NUMBER:
                if len(options) and val.isdigit():
                    if len(val) and int(val) in options.keys():
                        cb_val = int(val)
                        break

                elif val.isdigit() and len(val) >= minLen:
                    cb_val = val
                    break
                else:
                    print("INVALID: Only numbers are allowed with the minimum length of {}".format(minLen))
            
            elif inputType == InputType.CURRENCY:
                try:
                    cb_val = round(float(val),2)
                    break
                except ValueError:
                    print("INVALID: Please enter the right amount to deposit")
            else:
                break

        return cb_val
    