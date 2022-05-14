from utils.helper import formata_float_str_moeda


class Cartao:

    def __init__(self: object, nome: str, limite: float) -> None:
        self.__nome: str = nome
        self.__limite: float = limite


    @property
    def nome(self: object) -> int:
        return self.__nome


    @property
    def limite(self: object ) -> float:
        return self.__limite


    def verificar_limite(self: object, carrinho) -> int:
        valor_total: float = 0
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]

                if valor_total <= self.limite:
                    return 0


        return 1

    def comprar(self: object, valor: float) -> None:
        if self.limite >= valor:
            self.limite = self.limite - valor


    def __str__(self: object ) -> str:
        return f'Nome: {self.nome}\nLimite: {formata_float_str_moeda(self.limite)}\n'
