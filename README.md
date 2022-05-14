
    TESTE TECNICO FINAL  - SICRED ESTÁGIO DESENVOLVE TECH

Lógica de programação - Implementar as questões 1, 2 e 3
na linguagem de programação de sua preferência ou em português estruturado.

- Questão 1: Implementar um gerenciador de limite de cartão de credito.

        - As entradas são: limite e lista de compras;
        - A saída deve ser 1 se o limite foi excedido e 0 se o limite não foi;
        - O limite é excedido quando a soma das compras é maior que o limite

- Questão 2: Calcular o rendimento da poupança de acordo com os seguintes requisitos:

        - As entradas são: valor, quantidade de meses, taxa SELIC, e Taxa Referencial;
        - Se a SELIC estiver abaixo de 8.5, a poupança rende 70% de Taxa SELIC e Taxa Referencial (ao mês)
        - Se a SELIC estiver acima, a poupança rende 0.5% + Taxa Referencial (ao mês);
        - A saída deve ser o resultado do investimento (inicial + rendimento).

- Questão 3: Retorna não apenas o resultado, mas retorna de forma estruturada o valor inicial,
             resultado final do investimento e o resultado do rendimento mês a mês.

- Questão Bônus: Descrever ou escrever testes para garantir que o código funciona nos casos mais comuns
            (acima da SELIC, abaixo da SELIC, etc).



# Questão 1::

### Implementar um gerenciador de limite de cartão de credito.

        - As entradas são: limite e lista de compras;
        - A saída deve ser 1 se o limite foi excedido e 0 se o limite não foi;
        - O limite é excedido quando a soma das compras é maior que o limite
        
A versão simplificada da solução desta questão esta no arquivo teste_tecnico_sicredi.py
Trata-se de uma funçõa que recebe como parâmetros o valor do limite do cartão e uma dicionário contendo uma os 
itens do carrinho de compras e retorna 1 se o limite for excedido e retorna 0 se o limite não foi. (O limite é excedido 
quando a soma do valor dos itens no carrinho de compras é maior que o limite)



