
from typing import List, Dict

from models.cartao import Cartao
from models.produto import Produto



def gerenciador_limite1(cartao: Cartao, carrinho_compras: dict) -> int:
    valor_compra: int = 0
    for i in carrinho_compras.values():
        valor_compra += i
        print(valor_compra)
        if valor_compra <= cartao.limite:

            return 0

        else:

            return 1

def gerenciador_limite(cartao: Cartao, carrinho: List[Dict[Produto, int]]) -> int:
    valor_total: float = 0
    for item in carrinho:
        for dados in item.items():
            print(dados[0])
            print(f'Quantidade: {dados[1]}')
            valor_total += dados[0].preco * dados[1]

            if valor_total <= cartao.limite:
                return 0

            else:
                return 1
