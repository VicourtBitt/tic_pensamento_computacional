from modules.CleanTerminalModule import clean_terminal

class ListaDeCompras:
    lista_com_itens = []

    def __init__(self, username):
        self._username = username

    @property
    def username(self):
        return self._username
    
    def adicionar_na_lista(self):
        measure_unit = ["KG", "G", "L", "ML", "UN", "M", "CM"]
        while True:
            try:
                product_name = input("Qual o nome do produto? [SAIR]\n>>> ")

                if product_name == "SAIR":
                    print("Saindo da adição de itens")
                    break
                clean_terminal()

                print("Escolha uma unidade de medida: \nDe massa sólida: [KG]-[G]\nDe líquidos: [L]-[ML]\nUnitário: [UN]\nDe extensão: [M]-[CM]")
                product_measure = input(">>> ").upper()

                if remove_all_spaces(product_measure) not in measure_unit:
                    raise KeyError
                clean_terminal()

                product_units = input("Quantas unidades? (Em números): ")

                if not product_units.isnumeric():
                    raise ValueError
                clean_terminal()

                product_description = input("Insira uma breve descrição do produto:\n>>> ")

            except (KeyError, ValueError) as error:
                if isinstance(error, KeyError):
                    print("Escala de medida não existente.")

                elif isinstance(error, ValueError):
                    print("Quantidade inválida inserida")
            
                continue

            self.lista_com_itens.append({"nome": product_name, "medida": product_measure, "quantidade": product_units, "descricao": product_description})
            print(f"{product_name} foi adicionado na lista de compras")
    
    def pesquisar_item(self):
        filtro = input("Você quer pesquisar baseado em que? [NOME]-[MEDIDA]-[QUANTIDADE]\n>>> ").lower()
        valor = input("O que você quer procurar? ")
        new_list = [(enum, item) for (enum, item) in enumerate(self.lista_com_itens) if self.lista_com_itens[enum][filtro] == valor]

        if new_list == []:
            print("Nenhum resultado.") 
            return

        for (enum, obj) in new_list:
            print(f"{enum+1} | Produto: {obj['nome']} | Tamanho/Peso: {obj['medida']} | Quantidade: {obj['quantidade']} | Descrição: {obj['descricao']}")

    def listar_items(self):
        if self.lista_com_itens == []:
            print("Sem nenhum item na lista")
            return

        for enum, obj in enumerate(self.lista_com_itens):
            print(f"{enum+1} | Produto: {obj['nome']} | Tamanho/Peso: {obj['medida']} | Quantidade: {obj['quantidade']} | Descrição: {obj['descricao']}")

    def remover_item(self):
        listar = self.listar_items
        listar()
        to_remove = int(input("Qual item você deseja remover (por número da listagem)? "))
        pop_value = self.lista_com_itens.pop(to_remove-1)
        print(f"Produto {pop_value['nome']} foi removido")
            
    @classmethod
    def iniciar_compras(cls, username):
        return ListaDeCompras(username)
    

def remove_all_spaces(string):
    return " ".join(string.split())

# obj = ListaDeCompras.iniciar_compras("Victor Bittencourt")
# obj.adicionar_na_lista()
# obj.listar_items()
# obj.pesquisar_item()


