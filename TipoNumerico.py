"""
Tipo numérico
"""

# Se utilizar duas barras me retorna a parte inteira no numero
num = 5 / 2
print(num) # 2.5

num2 = 5 // 2
print(num2) # 2

# Potencia usa **
potencia = 5 ** 2
print(potencia) # 25

# podemos utilizar _ para representar separação de casas decimais
milhao = 1_000_000
print(milhao) # 1000000

# incremento += ou -= *= /=
inc = 42
inc += 1
print(inc) # 43

# para saber o tipo da variavel use a função type
n = 43
print(type(n)) # int
n /= 2
print(type(n)) # float
