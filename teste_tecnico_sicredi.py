
"""
QUESTÃO 1:
Está é uma implementação simplificada da Questão 1.
"""

credito: int = 5800
carrinho: dict = {
    "Playstation 4": 4500,
    "Xbox": 2500,
    "Nintendo Wii": 1800,
    "Techado mecânico gamer RGB Hyper X": 500,
}


def gerenciador_limite(limite: float, carrinho_compras: dict[str: float]) -> int:
    """
    A função recebe o valor do limite do cartão e um carrinho de compras e verifica se a compra dos itens do carrinho
    pode ser efetuada, retornando 1 caso o limite seja excedido e 0 caso contrario.
    """
    valores: list  = [valor for valor in carrinho_compras.values()]
    valor_compra: float = sum(valores)

    if valor_compra <= limite:

        return 0


    return 1

print(gerenciador_limite(credito, carrinho))


def test_gerenciador_limite():
    """Teste para verificar a função gerenciador_limite()"""
    carrinho_compras: dict = {
        "Playstation 4": 4500,
        "Xbox": 2500,
        "Nintendo Wii": 1800,
        "Techado mecânico gamer RGB Hyper X": 500,
    }
    assert gerenciador_limite(500, carrinho_compras) == 1

    assert gerenciador_limite(16000, carrinho_compras) == 0


test_gerenciador_limite()







