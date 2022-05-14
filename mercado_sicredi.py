from typing import List, Dict
from time import sleep


from models.cartao import Cartao
from models.produto import Produto
from utils.helper import formata_float_str_moeda

cartao: Cartao = Cartao("Marina Ruanna", 2700)
produtos : List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()

def menu() -> None:
    print('================================')
    print('======= Bem-vindo(a)! ==========')
    print('======= Sicredi Shop ===========')
    print('================================')


    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Adicionar ao carrinho')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair do sistema')


    try:
        opcao: int = int(input())

        if opcao == 1:
            cadastrar_produto()
        elif opcao == 2:
            listar_produtos()
        elif opcao == 3:
            adicionar_carrinho()
        elif opcao == 4:
            visualizar_carrinho()
        elif opcao == 5:
            fechar_pedido()
        elif opcao == 6:
            print('Volte sempre!')
            sleep(2)
            exit(0)
        else:
            print('Opção inválida!')
            sleep(1)
            menu()

    except ValueError:
        print("Opção inválida")
        menu()


def cadastrar_produto() -> None:
    """Cadastra produtos no mercado para que possam ser adicionados no carrinho"""
    print('Cadatro de produto')
    print('==================')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()

def listar_produtos() -> None:
    """lista os produtos já cadastrados informando seu codigo, nome e valor"""
    if len(produtos) > 0:
        print('Listagem de produtos')
        print('====================')
        for produto in produtos:
            print(produto)
            print('----------------')
            sleep(2)
    else:
        print('Ainda não existem produtos cadastrados.')
    sleep(2)
    menu()

def adicionar_carrinho() -> None:
    """Adiciona os produtos no carrinh"""
    if len(produtos) > 0:
        print('informe o código do produto que deseja adicionar no carrinho:')
        print('-------------------------------------------------------------')
        print('================== Produtos disponíveis =====================')
        for produto in produtos:
            print(produto)
            print('-------------------------------------------------------')
            sleep(2)
        codigo: int = int(input())

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho')
                sleep(2)
                menu()
        else:
            print(f'O produto com código {codigo} não foi encontrado.')
            sleep(2)
            menu()
    else:
        print('Ainda não existem produtos a venda.')
    sleep(2)
    menu()

def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho:')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-----------------------')
                sleep(1)
    else:
        print('O carrinho está vazio')
        print('---------------------')

    sleep(2)
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do carrinho')
        print('====================')
        if cartao.verificar_limite(carrinho) == 0:
            print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
            print(f'Compra autorizada! Obrigada e volte sempre!')
            cartao.comprar(valor_total)
            print(f'O limite do seu cartão agora é : {formata_float_str_moeda(cartao.limite)}')
            carrinho.clear()
            sleep(5)
            menu()
        else:
            print("Compra não autorizada, limite do cartão excedido")
            print("Seu carrinho foi esvaziado")
            sleep(2)
            carrinho.clear()
            menu()

    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(2)
    menu()

def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
