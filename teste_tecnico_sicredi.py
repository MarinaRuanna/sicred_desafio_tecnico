
"""
QUESTÃO 1:
"""
from random import randint


def cria_carrinho():

    carrinho_compras = []
    resposta: str =  's'

    while resposta != 'n' or resposta != 'N':
        if resposta == 's' or resposta == "S":
            try:
                nome: str = str(input('Informe o nome do produto: '))
                preco: float = float(input('Informe o preço do produto: '))
                quantidade: int = int(input("Informe a quantidade deste produto que deseja adicionar ao seu carrinho: "))

                produto = {"nome": nome,'preco': preco, 'quantidade': quantidade, 'valor_total': preco * quantidade}

                carrinho_compras.append(produto)
                print('\n--------------------')
                print('CARRINHO DE COMPRAS:')
                print('--------------------')
                for item in carrinho_compras:
                    for dados in item.items():
                        print(f'{dados[0]}: {dados[1]}')
                    print('-----------------------')

                print('\n')

                resposta: str = input("Deseja adicionar produtos ao seu carrinho? (s / n): ")

            except ValueError:
                print('Opção invalida')
                continue

        elif resposta == 'n' or resposta == "N":
            print('\n--------------------')
            print('CARRINHO DE COMPRAS:')
            print('--------------------')
            for item in carrinho_compras:
                for dados in item.items():
                    print(f'{dados[0]}: {dados[1]}')
                print('-----------------------')

            valores = [item['valor_total'] for item in carrinho_compras]
            total_compras = sum(valores)

            print(f'O valor total do seu carrinho é de: R$ {total_compras}')

            return carrinho_compras

        else:
            print('Opção inválida, sua sessão será encerrada')
            exit(0)




def gerenciador_limite(limite: float, carrinho_compras: list[dict]) -> int:

    valores = [item['valor_total'] for item in carrinho_compras]
    total_compras = sum(valores)

    if total_compras <= limite:
        return 0

    return 1



carrinho = cria_carrinho()
limite = randint(1, 100000)
print(f'O seu limite é de: R$ {limite}')

print(gerenciador_limite(limite, carrinho))




def test_gerenciador_limite():
    """Teste para verificar a função gerenciador_limite()"""
    carrinho_compras: list = [
        {'nome': 'Playstation 4', 'preco': 5800, 'quantidade': 1, 'valor_total': 1 * 5800},
        {'nome': 'Headset Corsair', 'preco': 230, 'quantidade': 3, 'valor_total': 230 * 3},
        {'nome': 'Mouse Redragon RGB', 'preco': 150, 'quantidade': 1, 'valor_total': 150 * 1},
        {'nome': 'Teclado mecânico gamer RGB Hyper X', 'preco': 500, 'quantidade': 5, 'valor_total': 500 * 5 }
    ]
    assert gerenciador_limite(500, carrinho_compras) == 1

    assert gerenciador_limite(10000, carrinho_compras) == 0

test_gerenciador_limite()







