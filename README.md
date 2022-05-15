
## SICRED ESTÁGIO DESENVOLVE TECH 
### TESTE TECNICO FINAL - (Lógica de programação)
### QUESTÃO 1:

### Implementar um gerenciador de limite de cartão de credito.
 - As entradas são: limite e lista de compras;
 - A saída deve ser 1 se o limite foi excedido e 0 se o limite não foi;
 - O limite é excedido quando a soma das compras é maior que o limite
 
 **Versão simplificada da resolução da questão:**
    
    def cria_carrinho():

    carrinho_compras = []
    resposta: str =  's'

    while resposta != 'n' or resposta != 'N':
        try:
            if resposta == 's' or resposta == "S":
                try:
                    nome: str = str(input('Informe o nome do produto: '))
                    preco: int = int(input('Informe o preço do produto: '))
                    quantidade: int = int(input("Informe a quantidade deste produto que deseja adicionar ao seu carrinho: "))

                    produto = {"nome": nome,'preco': preco, 'quantidade': quantidade, 'valor_total': preco * quantidade}

                    carrinho_compras.append(produto)
                    print(carrinho_compras)
                    print(type(carrinho_compras))

                    resposta: str = input("Deseja adicionar produtos ai seu carrinho? (s / n): ")

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

                print('\n')

                return carrinho_compras

            else:
                print('Opção inválida, sua sessão será encerrada')
                exit(0)


        except ValueError:
            print('Opção inválida, sua sessão será encerrada')
            exit(0)




    def gerenciador_limite(limite: float, carrinho_compras: list[dict]) -> int:
    
        valores = [item['valor_total'] for item in carrinho_compras]
        total_compras = sum(valores)
    
        if total_compras <= limite:
            return 0
    
        return 1
    
    
    
    carrinho = cria_carrinho()
    
    gerenciador_limite(5, carrinho)
    
    
    
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

### Resolução da questão:

O projeto mercado_sicredi utiliza POO, usando os objetos Produto e Cartao em um mercado simplificado, onde é possível:
 - cadastrar produtos;
 - listar produtos;
 - comprar produtos;
 - visualizar carrinho;
 - fechar pedido;
 - sair do sistema.

Na finalização da compra (fechar_pedido()) eu utilizei a função do objeto Cartao (cartao.verificar_limite()), baseada na Questão 1, 
que verifica se o limite disponível é compatível com o valor da compra e ,caso seja, esse valor é subtraído do limite do cartão (cartao.comprar()).


O fluxo de execução é:
- Cadastrar os produtos que deseja que estejam dispóniveis

- Adicionar ao carrinho de compras a partir do código gerado no cadastro do produto. Ao ser selecionada a opção Adicionar 
ao carrinho os produtos disponiveis serão listados.

- Fechar o pedido. Onde será verificado se o limite do cartão é suficiente para comprar os produtos. Caso não seja o 
carrinho sera esvaziado e o programa retornará para o menu inicial. (Os produtos cadastrados anteriormente ainda estarão disponiveis)



