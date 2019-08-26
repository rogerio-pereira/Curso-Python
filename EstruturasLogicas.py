"""
Estruturas lógicas
and, or, not, is

Operadores unários
    not
Operadores binários
    and, or, is
"""

ativo = True
logado = True

if ativo and logado:
    print('Bem-vindo usuário')
else:
    print('Você precisa precisa ativar sua conta, por favor cheque seu e-mail')

if not ativo:
    print('Você precisa precisa ativar sua conta, por favor cheque seu e-mail')

if ativo is True:
    print('Bem Vindo')