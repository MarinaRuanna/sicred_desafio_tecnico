
"""
QUESTÃO 1: Implementar um gerenciador de limite de cartão de credito.

  - As entradas são: limite e lista de compras;
  - A saída deve ser 1 se o limite foi excedido e 0 se o limite não foi;
  - O limite é excedido quando a soma das compras é maior que o limite

"""
def main():
    limite = int(input("Digite o limite do seu cartão: "))
    carrinho = cria_carrinho()
    print(f'O seu limite é de: R$ {limite}')
    compra = gerenciador_limite(limite, carrinho)
    if compra:
        print('Compra não aprovada, limite do cartão ecxedido')

    else:
        print("Compra aprovada! Obrigada, volte sempre!")




def gerenciador_limite(limite: float, lista_compras: list[dict]) -> int:
    """
    Como exigido na QUESTÃO 1, a função recebe o valor do limite do cartão e um carrinho de compras
    e verifica se a compra dos itens do carrinho pode ser efetuada,
    retornando 1 caso o limite seja excedido e 0 caso contrario.
    """
    valores = [item['valor_total'] for item in lista_compras]
    total_compras = sum(valores)

    if total_compras <= limite:
        return 0

    return 1



def cria_carrinho():
    """
    Implementei essa função para dar entrada na função gerenciador_limite() através de uma interação com o usuário
    Função que gera uma lista de dicionários que representam produtos armazenados pelo usuário.
    :return: list[carrinho_compras]
    """
    carrinho_compras = []
    resposta: str =  's'

    while resposta != 'n' or resposta != 'N':
        if resposta == 's' or resposta == "S":
            try:
                """
                Testa se os valores inseridos pelo usúario correspondem aos esperados para a criação do produto
                """
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

            except ValueError: #
                """
                Caso o usúario digite um valor inválido esse produto será descartado e ele poderá 
                continuar adicionando produtos sem afetar o carrinho
                """
                print('Opção invalida')
                continue

        elif resposta == 'n' or resposta == "N":
            """
            Após adicionar todos os produtos que deseja o usúario encerra a 
            aplicação e é exibido todos os itens do carrinho e o valor total da compra
            """
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


def test_gerenciador_limite():
    """
    Teste para verificar a função gerenciador_limite()
    """
    lista_compras: list = [
        {'nome': 'Playstation 4', 'preco': 5800, 'quantidade': 1, 'valor_total': 1 * 5800},
        {'nome': 'Headset Corsair', 'preco': 230, 'quantidade': 3, 'valor_total': 230 * 3},
        {'nome': 'Mouse Redragon RGB', 'preco': 150, 'quantidade': 1, 'valor_total': 150 * 1},
        {'nome': 'Teclado mecânico gamer RGB Hyper X', 'preco': 500, 'quantidade': 5, 'valor_total': 500 * 5 }
    ]
    assert gerenciador_limite(500, lista_compras) == 1

    assert gerenciador_limite(10000, lista_compras) == 0

test_gerenciador_limite()


if __name__ == '__main__':
    main()













