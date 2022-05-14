
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
            print('\n--------------------')
            print('CARRINHO DE COMPRAS:')
            print('--------------------')
            for item in carrinho_compras:
                for i in item.items():
                    print(i)



            print('-----------------------')

            print('\n')

            return carrinho_compras


def gerenciador_limite(limite: float, carrinho_compras: list[dict]) -> int:
    total_compras = 0
    for item in carrinho_compras:
        for i in item.values():
            total_compras = total_compras + i

        if total_compras <= limite:
            return 0

    return 1


"""
    total_compra: float = 0
    for i in carrinho_compras:
        for j in i.items():
            for dados in j.items():
            total_compra = total_compra + dados[3]

        if total_compra <= limite:
            return 0

    return 1
    
    
    
            for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                
  valores: list = [item for item in carrinho_compras[]]
    valor_compra: float = sum(valores)

    if valor_compra <= limite:
        return 0

    return 1
"""

carrinho = cria_carrinho()

print(gerenciador_limite(5000, carrinho))



