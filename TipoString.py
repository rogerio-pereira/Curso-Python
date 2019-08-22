"""
Tipo String

Em python um dado é considerado string se estiver entre aspas simples
    'string'
    '123'
    'True'
    '3.14'
Sempre que estiver entre aspas duplas
    "string"
    "123"
    "True"
    "3.14"
Estiver entre aspas simples triplas
Estiver entre aspas duplas triplas
"""

newLine = 'new\nline'
print(newLine)
newLine = """new
line"""
print(newLine)

nome = 'Rogerio Pereira'
print(nome.upper())
print(nome.lower())
print(nome.split()) # Transforma em uma lista de Strings
nome2 = ' Teste'
print(nome + nome2)

# Internamente o Python converte uma string em uma lista de caracteres
print(nome[0:4]) # Começando da posição 0 indo até a posição 4
print(nome.split()[0]) # Transforma em uma lista de string e pega a primeira
print(nome.split()[1])

# inversão de String
# [::-1] - Começa do primeiro elemento, vá até o ultimo elemento e inverta
print(nome[::-1])

