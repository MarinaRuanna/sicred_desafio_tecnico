
def cria_carrinho():

    carrinho_compras = []
    resposta: str =  's'
    while resposta != 'n' or resposta != 'N':
        if resposta == 's' or resposta == "S":

            nome: str = str(input('Informe o nome do produto: '))
            preco: float = float(input('Informe o preço do produto: '))
            quantidade: int = int(input("Informe a quantidade deste produto que deseja adicionar ao seu carrinho: "))

            produto = {"nome": nome,'preco': preco, 'quantidade': quantidade, 'valor_total': preco * quantidade}

            carrinho_compras.append(produto)




            print(carrinho_compras)
            print(type(carrinho_compras))

            resposta: str = input("Deseja adicionar produtos ai seu carrinho? (s / n): ")

        elif resposta == 'n' or resposta == "N":
            valor_total = 0
            print('\n--------------------')
            print('CARRINHO DE COMPRAS:')
            print('--------------------')
            for item in carrinho_compras:
                for dados in item.items():
                    print(f'{dados[0]}: {dados[1]}')
                print('-----------------------')

            print('\n')

            return carrinho_compras


def gerenciador_limite(limite: float, carrinho_compras: list[dict]) -> int:
    total_compras = 0

    for item in carrinho_compras:
        for i in item.items():
            total_compras = total_compras + item['valor_total']

    if total_compras <= limite:
        return 0

    return 1


carrinho = cria_carrinho()

print(gerenciador_limite(5, carrinho))



