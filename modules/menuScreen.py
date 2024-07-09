from modules.CleanTerminalModule import clean_terminal

def _menu_screen():
    _menu_special_char = "—"
    _menu_greetings_text = "BEM VINDO(A) A LISTA DE COMPRAS!"
    _mgt_lenght = len(_menu_greetings_text)
    _horizontal_rule = f"{_menu_special_char*(int(_mgt_lenght*2))}"
    _half_hr = f'{_menu_special_char*int(_mgt_lenght/2)}'

    print(f"{_horizontal_rule}")
    print(f"{_half_hr}{_menu_greetings_text}{_half_hr}")
    print(f"{_horizontal_rule}")
    print()


def _get_username():
    while True:    
        try:
            _username = input("Insira seu nome de usuário: ").upper()
            if len(_username) < 3:
                raise TypeError  

            elif _username.isnumeric():
                raise ValueError

        except (ValueError, TypeError) as error:
            clean_terminal()

            if isinstance(error, ValueError):
                print("Erro 'Nome em Numeros'. O nome de usuário não pode ser composto somente de numerais.")

            elif isinstance(error, TypeError):
                print("Erro 'Nome Curto'. Escreva um nome de usuário maior.")

            continue

        clean_terminal()
        return _username