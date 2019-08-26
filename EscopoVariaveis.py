"""
Escopo de Variáveis

Dois casos de escopo
1 - Variaveis globais
    São reconhecidas, ou seja, seu escopo compreende todo o programa
2 - Variaveis locais
    São reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está limitado ao bloco
        onde foi declarada

Para declarar variaveis em Python fazemos:
    nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinamica. Isso significa que ao declararmos uma variavel nós não colocamos
    o tipo de dados dela, esse tipo é inferido ao atribuirmos o valor à mesma

    Exemplo em C
    int numero = 42;
"""

numero = 42  # Exemplo de variavel global
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

numero = 2
novo = 0  # Criando variavel para não dar erro

if numero > 10:
    novo = numero + 10  # Exemplo de variavel local (dentro do escopo do if)
    print(novo)

print(novo)  # Vai dar um erro de execução, pq novo não foi criado, para corrigir precisamos criar a variavel