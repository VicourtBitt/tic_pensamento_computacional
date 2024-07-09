from modules.CleanTerminalModule import clean_terminal
from modules.ListaDeCompras import ListaDeCompras


def _options_screen(username, obj):

    dict_options = {
        "ADICIONAR" : obj.adicionar_na_lista,
        "LISTAR": obj.listar_items,
        "REMOVER" : obj.remover_item,
        "PESQUISAR" : obj.pesquisar_item,
    }   

    while True:
        print(f"Seja bem vindo(a) {username}.")
        print("Escolha uma das seguintes opções: [ADICIONAR]-[LISTAR]-[REMOVER]-[PESQUISAR]-[SAIR]")
        try: 
            decision = input(">>> ").upper()

            if decision.isnumeric():
                raise ValueError

            elif decision not in dict_options:
                raise KeyError
                        
        except (KeyError, ValueError) as error:
            clean_terminal()

            if isinstance(error, ValueError):
                print(f"Insira uma opção, não um número. Inserido= {decision}")

            elif isinstance(error, KeyError):
                print(f"Esta opção não existe. Inserido= {decision}")

            continue

        clean_terminal()
        if decision == "ADICIONAR":
            dict_options["ADICIONAR"]()
            
        elif decision == "LISTAR":
            dict_options["LISTAR"]()

        elif decision == "REMOVER":
            dict_options["REMOVER"]()

        elif decision == "PESQUISAR":
            dict_options["PESQUISAR"]()

        elif decision == "SAIR":
            break