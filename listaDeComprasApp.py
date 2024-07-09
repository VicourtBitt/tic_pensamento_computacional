from modules.CleanTerminalModule import clean_terminal
from modules.ListaDeCompras import ListaDeCompras
from modules.menuScreen import _menu_screen, _get_username
from modules.options import _options_screen

# _menu_screen()
# nome = _get_username
# print(f"Seja bem vindo(a): {nome()}")

def main():
    username = ""
    while True:
        _menu_screen()
        
        if username == "":
            username = _get_username()

        obj = ListaDeCompras.iniciar_compras(username)

        _options_screen(username, obj)

if __name__ == "__main__":
    main()