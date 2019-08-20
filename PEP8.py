"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

import this
    Use esse comando para ver o poema "The Zem of Python"

A idéia da PEP8 é que possamos escrever códigos Python de forma Pythônica
    1 - Utilize CamelCase para nomes de classes
    2 - Utilize nomes em minusculo separados por _ para funções ou variaveis
    3 - Utilize 4 espaços para identação
    4 - Linhas em branco
        2 antes de classes e funções
        1 antes de métodos dentro de classes
    5 - Imports
        Imports devem ser sempre feitos em linhas separadas
        Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentarios e docstrings e
            antes de constantes e variaveis globais
    6 - Espaços em expressões e instruções
    7 - Termine sempre uma instrução com uma nova linha
        Linha 95
"""


"""1"""


class Calculadora:
    pass


class CalculadoraCietifica:
    pass


"""2"""
def soma():
    pass


def soma_dois():
    pass


numero = 4
numero_impar = 3


"""3"""
if 'a' in 'banana':
    print('tem')


"""5"""
# Errado
# import sys, os

# Certo
import sys
import os

# Não há problemas em utilizar
from types import StringType, ListType

# Casos tenha muitos imports de um mesmo pacotes, recomenda-se fazer
"""from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)"""


"""6"""
# NÃO FAÇA
# funcao( algo[ 1 ], { outro: 2 } )
# algo (1)
# dict ['chave'] = lista [indice]

# x                 = 1
# y                 = 2
# variavel_longa    = 3

# FAÇA:
# funcao(algo[1], {outro: 2})
# algo(1)
# dict['chave'] = lista[indice]

# x = 1
# y = 2
# variavel_longa = 3

import this
