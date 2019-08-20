"""
Recebendo dados do usuário

input() -> Todo dado recebido em um imput é uma string

Em Python string é tudo o que estiver entre
    aspas simples
        'Rogerio Pereira'
    aspas duplas
        "Rogerio Pereira"
    aspas simples triplas
        '''Rogerio Pereira'''
    aspas duplas triplas
"""
#       """Rogerio Pereira"""

# Entrada de Dados
"""
print("Qual o seu nome?")
nome = input() # input -> Entrada
"""
nome = input('Qual o seu nome? ')

# Exemplo de print antigo 2.x
# print('Seja bem-vindo(a) %s' % nome)
# Print moderno 3.x
# print('Seja bem-vindo {0}'.format(nome))
# Print mais atual 3.7
print(f'Seja bem-vindo {nome}')

"""
print("Qual a sua idade?")
idade = input()
"""
idade = int(input('Qual a sua idade? '))

# Processamento

# Saida de dados
# Exemplo de print antigo 2.x
# Se tiver um ou mais parametros para impressão, é necessário parenteses
# print('O(a) %s tem %s anos' % (nome, idade))
# Print moderno 3.x
# print('O(a) {0} tem {1} anos'.format(nome, idade))
# Print mais atual 3.7
print(f'O(a) {nome} tem {idade} anos')

"""
É necessario fazer um cast para a soma 
"""
print(f'O(a) {nome} nasceu em  {2019 - idade}')


