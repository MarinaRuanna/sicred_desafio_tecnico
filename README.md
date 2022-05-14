
## SICRED ESTÁGIO DESENVOLVE TECH 
### TESTE TECNICO FINAL - (Lógica de programação)
### QUESTÃO 1:

### Implementar um gerenciador de limite de cartão de credito.
 - As entradas são: limite e lista de compras;
 - A saída deve ser 1 se o limite foi excedido e 0 se o limite não foi;
 - O limite é excedido quando a soma das compras é maior que o limite
 
 **Versão simplificada da resolução da questão:**
    
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



